-- Migration 0001: initial schema (categories, authors, books,
-- book_authors, book_related, users, conversations, messages,
-- announcements). Equivalent to the old flat schema.sql, kept here
-- as the first entry in a versioned migration history.

CREATE DATABASE IF NOT EXISTS askmql CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE askmql;

CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE authors (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL
);

CREATE TABLE books (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  isbn VARCHAR(20),
  publication_year INT,
  description TEXT,
  shelf_code VARCHAR(50),
  location_notes VARCHAR(150),
  cover_color VARCHAR(10) DEFAULT '#2563EB',
  cover_icon VARCHAR(50) DEFAULT 'book',
  is_available BOOLEAN NOT NULL DEFAULT TRUE,
  category_id INT,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

CREATE TABLE book_authors (
  book_id INT NOT NULL,
  author_id INT NOT NULL,
  PRIMARY KEY (book_id, author_id),
  FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
  FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

CREATE TABLE book_related (
  book_id INT NOT NULL,
  related_book_id INT NOT NULL,
  PRIMARY KEY (book_id, related_book_id),
  FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
  FOREIGN KEY (related_book_id) REFERENCES books(id) ON DELETE CASCADE
);

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  student_id VARCHAR(30),
  department VARCHAR(100),
  avatar_initials VARCHAR(4)
);

CREATE TABLE conversations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(150) NOT NULL DEFAULT 'New conversation',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  conversation_id INT NOT NULL,
  role ENUM('user','ai') NOT NULL,
  content TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
);

CREATE TABLE announcements (
  id INT AUTO_INCREMENT PRIMARY KEY,
  message VARCHAR(255) NOT NULL,
  posted_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_books_title ON books(title);
CREATE INDEX idx_messages_conversation ON messages(conversation_id);
