"""Keyword/category retrieval against MySQL -- today's only real
search path. This is intentionally simple; fusion.py is the seam
where semantic.py's results get merged in once embeddings exist."""
from repositories.book_repository import BookRepository

_repo = BookRepository()

_CATEGORY_KEYWORDS = [
    ("artificial intelligence", "Artificial Intelligence"),
    (" ai ", "Artificial Intelligence"),
    ("machine learning", "Artificial Intelligence"),
    ("program", "Programming"),
    ("database", "Databases"),
    ("network", "Networking"),
]


def search(text: str):
    text_l = f" {text.lower()} "

    title_hit = _repo.title_like(text)
    if title_hit:
        return title_hit

    for keyword, category_name in _CATEGORY_KEYWORDS:
        if keyword in text_l:
            books = _repo.by_category_name(category_name)
            if category_name == "Programming":
                books += _repo.by_category_name("Software Engineering")
            if books:
                return books

    words = [w for w in text_l.split() if len(w) > 3]
    if not words:
        return []

    all_books = _repo.all()
    return [
        b
        for b in all_books
        if any(w in b.title.lower() for w in words)
        or any(w in a.name.lower() for a in b.authors for w in words)
    ]
