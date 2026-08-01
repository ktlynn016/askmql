"""Post-retrieval filters (availability, category) applied after
ranking so they don't distort relevance scoring upstream."""


def only_available(books: list):
    return [b for b in books if b.is_available]


def by_category(books: list, category_name: str):
    return [b for b in books if b.category and b.category.name == category_name]
