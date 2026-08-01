from database.db import db

book_authors = db.Table(
    "book_authors",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id"), primary_key=True),
    db.Column("author_id", db.Integer, db.ForeignKey("authors.id"), primary_key=True),
)

book_related = db.Table(
    "book_related",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id"), primary_key=True),
    db.Column("related_book_id", db.Integer, db.ForeignKey("books.id"), primary_key=True),
)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(20))
    publication_year = db.Column(db.Integer)
    description = db.Column(db.Text)
    shelf_code = db.Column(db.String(50))
    location_notes = db.Column(db.String(150))
    cover_color = db.Column(db.String(10), default="#2563EB")
    cover_icon = db.Column(db.String(50), default="book")
    is_available = db.Column(db.Boolean, default=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    # Populated later by jobs/refresh_embeddings.py once an embeddings
    # provider is configured; NULL/unused under the default "none" provider.
    embedding_updated_at = db.Column(db.DateTime, nullable=True)

    authors = db.relationship("Author", secondary=book_authors, backref="books")

    related_books = db.relationship(
        "Book",
        secondary=book_related,
        primaryjoin=id == book_related.c.book_id,
        secondaryjoin=id == book_related.c.related_book_id,
    )

    def to_dict(self, include_related=False):
        data = {
            "id": self.id,
            "title": self.title,
            "author": ", ".join(a.name for a in self.authors),
            "category": self.category.name if self.category else None,
            "year": self.publication_year,
            "isbn": self.isbn,
            "description": self.description,
            "shelf": self.shelf_code,
            "location": self.location_notes,
            "available": bool(self.is_available),
            "color": self.cover_color,
            "icon": self.cover_icon,
        }
        if include_related:
            data["related"] = [b.id for b in self.related_books]
        return data
