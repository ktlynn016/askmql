-- Migration 0002: analytics tables (feedback, query_logs) and an
-- embeddings-readiness column on books, backing services/analytics/*
-- and the future semantic retrieval path.

USE askmql;

CREATE TABLE feedback (
  id INT AUTO_INCREMENT PRIMARY KEY,
  message_id INT NOT NULL,
  rating ENUM('up','down') NOT NULL,
  note VARCHAR(500),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (message_id) REFERENCES messages(id) ON DELETE CASCADE
);

CREATE TABLE query_logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  conversation_id INT,
  query_text TEXT NOT NULL,
  intent VARCHAR(50),
  result_count INT DEFAULT 0,
  latency_ms INT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE SET NULL
);

ALTER TABLE books ADD COLUMN embedding_updated_at DATETIME NULL;

CREATE INDEX idx_query_logs_created ON query_logs(created_at);
