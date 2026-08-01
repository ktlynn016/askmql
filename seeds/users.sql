-- Demo accounts for local development/testing. Run after
-- migrations/0003_add_auth.sql. Passwords are real, hashed with
-- Werkzeug's scrypt-based generate_password_hash -- these are NOT
-- placeholder/plaintext values, they'll actually work against
-- POST /api/v1/auth/login.
--
-- Demo student  -- student_id: 2023-0114  password: student123
-- Demo librarian -- email: librarian@gsu-mosqueda.edu.ph  password: librarian123
--
-- Change or remove both before any real deployment.

USE askmql;

INSERT INTO users (id, name, role, email, password_hash, student_id, department, avatar_initials) VALUES
  (1, 'Jamie Cruz', 'student', NULL,
   'scrypt:32768:8:1$rfDGmgBM3slCpHcR$3cd1c628224e57853b3d5db7550ea20cb856e0f591fb62923bb58dfff61b9e641238c057d02a514c24ff0872bc88fcf715c4e75e114dbb2e876ae9e17f5e8017',
   '2023-0114', 'BSIT', 'JC'),
  (2, 'Maria Santos', 'librarian', 'librarian@gsu-mosqueda.edu.ph',
   'scrypt:32768:8:1$Lgw2DghMKRQqwUyv$986725b9f5204f4246de0ad68d81636f36c2a6f1159c9424d05f299a85563ac88143b1134e8d7b64a7e263a6314c669af829264470f8a366d97309e877ebb1c5',
   NULL, 'Library Staff', 'MS');
