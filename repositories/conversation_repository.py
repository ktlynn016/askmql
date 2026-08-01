from datetime import datetime

from models.conversation import Conversation
from models.message import Message
from repositories.base import BaseRepository


class ConversationRepository(BaseRepository):
    def get(self, conversation_id):
        return Conversation.query.get(conversation_id)

    def list(self):
        return Conversation.query.order_by(Conversation.updated_at.desc()).all()

    def create(self, title="New conversation"):
        conv = Conversation(title=(title or "New conversation")[:150])
        self._add(conv)
        self._commit()
        return conv

    def get_or_create(self, conversation_id, seed_title=None):
        if conversation_id:
            conv = self.get(conversation_id)
            if conv:
                return conv
        return self.create((seed_title or "New conversation")[:40])

    def rename(self, conversation_id, title):
        conv = self.get(conversation_id)
        if not conv or not title:
            return None
        conv.title = title[:150]
        self._commit()
        return conv

    def delete(self, conversation_id):
        conv = self.get(conversation_id)
        if not conv:
            return False
        from database.db import db

        db.session.delete(conv)
        self._commit()
        return True

    def messages(self, conversation_id):
        return (
            Message.query.filter_by(conversation_id=conversation_id)
            .order_by(Message.created_at.asc())
            .all()
        )

    def add_message(self, conversation_id, role, content):
        msg = Message(conversation_id=conversation_id, role=role, content=content)
        self._add(msg)
        conv = self.get(conversation_id)
        if conv:
            conv.updated_at = datetime.utcnow()
        self._commit()
        return msg
