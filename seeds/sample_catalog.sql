-- Sample catalog data for local development. Mirrors the frontend's
-- dummy dataset so the UI and the real API return matching results.
-- Run after migrations 0001 and 0002. Replace with the real GSU
-- Mosqueda Campus Library catalog for production (or point
-- jobs/sync_catalog.py at a real feed adapter instead).

USE askmql;

INSERT INTO categories (id, name) VALUES
  (1, 'Artificial Intelligence'),
  (2, 'Software Engineering'),
  (3, 'Programming'),
  (4, 'Databases'),
  (5, 'Networking');

INSERT INTO authors (id, name) VALUES
  (1, 'Stuart Russell'), (2, 'Peter Norvig'), (3, 'Ian Goodfellow'),
  (4, 'Yoshua Bengio'), (5, 'Aaron Courville'), (6, 'Robert C. Martin'),
  (7, 'David Thomas'), (8, 'Andrew Hunt'), (9, 'Thomas H. Cormen'),
  (10, 'Charles E. Leiserson'), (11, 'Ronald L. Rivest'), (12, 'Clifford Stein'),
  (13, 'Andrew Ng'), (14, 'Abraham Silberschatz'), (15, 'Henry F. Korth'),
  (16, 'S. Sudarshan'), (17, 'Ramez Elmasri'), (18, 'Shamkant B. Navathe'),
  (19, 'James Kurose'), (20, 'Keith Ross'), (21, 'Wendell Odom');

INSERT INTO books
  (id, title, isbn, publication_year, description, shelf_code, location_notes, cover_color, cover_icon, is_available, category_id)
VALUES
  (1, 'Artificial Intelligence: A Modern Approach', '978-0134610993', 2020,
   'The standard reference on AI, covering search, knowledge representation, machine learning, and reasoning under uncertainty.',
   'QA76.5 R87', '2F · AI & Computing · Aisle 3', '#2563EB', 'brain', TRUE, 1),
  (2, 'Deep Learning', '978-0262035613', 2016,
   'A comprehensive introduction to deep learning, from linear algebra foundations to convolutional and recurrent networks.',
   'QA76.87 G66', '2F · AI & Computing · Aisle 3', '#1D4ED8', 'network-wired', FALSE, 1),
  (3, 'Clean Code: A Handbook of Agile Software Craftsmanship', '978-0132350884', 2008,
   'A practical guide to writing readable, maintainable code, with concrete rules for naming, functions, and structure.',
   'QA76.76 M368', '2F · Programming · Aisle 1', '#0EA5E9', 'broom', TRUE, 2),
  (4, 'The Pragmatic Programmer', '978-0135957059', 2019,
   'Field-tested advice on software craftsmanship, debugging habits, automation, and testing.',
   'QA76.6 T458', '2F · Programming · Aisle 1', '#3B82F6', 'code', TRUE, 3),
  (5, 'Introduction to Algorithms', '978-0262046305', 2022,
   'The definitive text on algorithms and data structures, covering sorting, graphs, and dynamic programming.',
   'QA76.6 C662', '2F · Programming · Aisle 1', '#1E40AF', 'diagram', TRUE, 3),
  (6, 'Machine Learning Yearning', '978-1720344306', 2018,
   'A practical playbook for structuring machine learning projects and diagnosing model errors.',
   'Q325.5 N43', '2F · AI & Computing · Aisle 3', '#60A5FA', 'chart-line', TRUE, 1),
  (7, 'Database System Concepts', '978-0078022159', 2019,
   'A thorough treatment of relational databases, SQL, transactions, indexing, and normalization.',
   'QA76.9 S497', '1F · Databases & Networks · Aisle 5', '#0284C7', 'database', TRUE, 4),
  (8, 'Fundamentals of Database Systems', '978-0133970777', 2015,
   'Covers database design, ER modeling, normalization, and query optimization.',
   'QA76.9 E46', '1F · Databases & Networks · Aisle 5', '#0369A1', 'server', FALSE, 4),
  (9, 'Computer Networking: A Top-Down Approach', '978-0136681557', 2020,
   'Introduces networking from the application layer down, using the internet as the primary example.',
   'TK5105.5 K88', '1F · Databases & Networks · Aisle 6', '#0891B2', 'network-wired', TRUE, 5),
  (10, 'CCNA 200-301 Official Cert Guide', '978-0135792735', 2019,
   'An exam-focused but practical guide to networking fundamentals, IP addressing, routing, and switching.',
   'TK5105.5 O36', '1F · Databases & Networks · Aisle 6', '#155E75', 'router', TRUE, 5);

INSERT INTO book_authors (book_id, author_id) VALUES
  (1,1),(1,2), (2,3),(2,4),(2,5), (3,6), (4,7),(4,8),
  (5,9),(5,10),(5,11),(5,12), (6,13), (7,14),(7,15),(7,16),
  (8,17),(8,18), (9,19),(9,20), (10,21);

INSERT INTO book_related (book_id, related_book_id) VALUES
  (1,2),(2,1), (1,6),(6,1), (2,6),(6,2),
  (3,4),(4,3), (3,5),(5,3), (4,5),(5,4),
  (7,8),(8,7), (9,10),(10,9);

-- Demo user accounts (student + librarian, with real password hashes)
-- live in seeds/users.sql -- run that after migration 0003_add_auth.sql.
