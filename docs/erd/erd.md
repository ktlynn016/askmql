# ASKMQL Entity-Relationship Diagram

```mermaid
erDiagram
    CATEGORIES ||--o{ BOOKS : has
    BOOKS }o--o{ AUTHORS : "written by (book_authors)"
    BOOKS }o--o{ BOOKS : "related to (book_related)"
    CONVERSATIONS ||--o{ MESSAGES : contains
    MESSAGES ||--o{ FEEDBACK : rated_by
    CONVERSATIONS ||--o{ QUERY_LOGS : logs

    CATEGORIES {
        int id PK
        string name
    }
    AUTHORS {
        int id PK
        string name
    }
    BOOKS {
        int id PK
        string title
        string isbn
        int publication_year
        text description
        string shelf_code
        string location_notes
        string cover_color
        string cover_icon
        bool is_available
        int category_id FK
        datetime embedding_updated_at
    }
    USERS {
        int id PK
        string name
        enum role "student | librarian"
        string email "librarian login; unique, nullable"
        string password_hash
        string student_id "student login; unique, nullable"
        string department
        string avatar_initials
    }
    CONVERSATIONS {
        int id PK
        string title
        datetime created_at
        datetime updated_at
    }
    MESSAGES {
        int id PK
        int conversation_id FK
        enum role
        text content
        datetime created_at
    }
    FEEDBACK {
        int id PK
        int message_id FK
        enum rating
        string note
        datetime created_at
    }
    QUERY_LOGS {
        int id PK
        int conversation_id FK
        text query_text
        string intent
        int result_count
        int latency_ms
        datetime created_at
    }
    ANNOUNCEMENTS {
        int id PK
        string message
        datetime posted_at
    }
```

## Notes

- `book_authors` and `book_related` are pure join tables (no
  attributes of their own), collapsed into the `}o--o{` relationships
  above rather than modeled as separate entities.
- `USERS` now carries login credentials (`role`, `email`/`student_id`,
  `password_hash` — see `docs/adr/0003-session-cookie-auth.md`) but
  still isn't linked to `CONVERSATIONS` — chat history stays anonymous
  for this milestone. Add a `user_id` FK on `conversations` if
  per-account history becomes a requirement.
- `embedding_updated_at` on `BOOKS` is unused until an embeddings
  provider is configured (see `docs/adr/0002-retrieval-adapter-seam.md`).
- Source of truth for the actual DDL is `backend/migrations/*.sql`;
  this file is documentation, not something migrations are generated
  from.
