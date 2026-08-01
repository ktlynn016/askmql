-- Migration 0003: authentication. Adds role/password/email to users
-- so the same table serves both student and librarian accounts.

USE askmql;

ALTER TABLE users
  ADD COLUMN role ENUM('student','librarian') NOT NULL DEFAULT 'student' AFTER name,
  ADD COLUMN email VARCHAR(150) NULL UNIQUE AFTER role,
  ADD COLUMN password_hash VARCHAR(255) NULL AFTER email,
  MODIFY COLUMN student_id VARCHAR(30) NULL UNIQUE;

CREATE INDEX idx_users_role ON users(role);
