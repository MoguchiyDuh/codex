# SQL & PostgreSQL Ultimate Cheat Sheet

## 1. Data Types & Enums

### Core Types

```sql
INT / BIGINT          -- Whole numbers (4 / 8 bytes)
DECIMAL(10,2)         -- Exact precision (Total digits, decimal places)
SERIAL / BIGSERIAL    -- Auto-incrementing IDs
FLOAT / REAL          -- Floating point
VARCHAR(n) / TEXT     -- Variable length strings (n limit vs unlimited)
BOOLEAN               -- TRUE, FALSE, NULL
DATE / TIMESTAMP      -- '2024-01-01', '2024-01-01 12:00:00'
INTERVAL              -- '1 day', '2 hours'
JSONB                 -- Binary JSON (indexed, preferred over JSON)
BYTEA                 -- Binary data (blobs)
```

### Custom Enums (Standard in Postgres)

```sql
CREATE TYPE user_role AS ENUM ('admin', 'editor', 'viewer');
ALTER TYPE user_role ADD VALUE 'moderator' AFTER 'editor'; -- Extend enum
```

---

## 2. DDL - Schema Definition

### CREATE TABLE with Constraints

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INT CHECK (age >= 18),
    role user_role DEFAULT 'viewer',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE, -- Foreign Key
    title TEXT NOT NULL,
    body TEXT
);
```

### ALTER TABLE (The Heavy Lifters)

```sql
ALTER TABLE users ADD COLUMN phone_number VARCHAR(20);
ALTER TABLE users DROP COLUMN phone_number;
ALTER TABLE users RENAME COLUMN email TO user_email;
ALTER TABLE users ALTER COLUMN age SET NOT NULL;
ALTER TABLE users ALTER COLUMN age DROP NOT NULL;
ALTER TABLE users ALTER COLUMN age TYPE BIGINT;
ALTER TABLE posts ADD CONSTRAINT unique_title UNIQUE (title);
```

---

## 3. DML - Data Manipulation

### INSERT (The Power Moves)

```sql
INSERT INTO users (email, age) VALUES ('test@ex.com', 25) RETURNING id; -- Get ID back
INSERT INTO posts (user_id, title) SELECT id, 'Welcome' FROM users;    -- Insert from Select
```

### UPDATE & DELETE

```sql
UPDATE users SET age = age + 1 WHERE id = 1;
UPDATE posts SET title = 'Draft' FROM users WHERE posts.user_id = users.id AND users.role = 'admin'; -- Join Update
DELETE FROM users WHERE id = 1;
TRUNCATE TABLE users RESTART IDENTITY CASCADE; -- Fast wipe, reset counters
```

---

## 4. DQL - The Join Guide

| Join Type      | Description                                                     |
| :------------- | :-------------------------------------------------------------- |
| **INNER JOIN** | Only rows with matches in BOTH tables.                          |
| **LEFT JOIN**  | ALL rows from Left + matching rows from Right. (Most common)    |
| **RIGHT JOIN** | ALL rows from Right + matching rows from Left.                  |
| **FULL JOIN**  | ALL rows from both tables, filling NULLs where no match exists. |
| **CROSS JOIN** | Cartesian product (every Row A with every Row B).               |
| **SELF JOIN**  | Joining a table to itself (e.g., manager/employee).             |

```sql
SELECT u.email, p.title
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
WHERE p.id IS NULL; -- Find users with NO posts
```

---

## 5. Queries, Aggregates & Transactions

### Aggregates

```sql
SELECT role, COUNT(*), AVG(age)
FROM users
GROUP BY role
HAVING COUNT(*) > 5; -- Filter grouped results
```

### CTEs (Common Table Expressions)

Clean, readable subqueries.

```sql
WITH user_posts AS (
    SELECT user_id, COUNT(*) as post_count
    FROM posts
    GROUP BY user_id
)
SELECT u.email, up.post_count
FROM users u
JOIN user_posts up ON u.id = up.user_id;
```

### Transactions (ACID)

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT; -- OR ROLLBACK; on failure
```

---

## 6. psql CLI & Postgres Power Features

### Meta-commands (\)

```text
\l          -- List databases
\c dbname   -- Connect to database
\dt         -- List tables ("describe tables")
\d table    -- Describe table schema/indexes
\dn         -- List schemas
\df         -- List functions
\x          -- Toggle expanded display (vertical rows, great for wide tables)
\copy table TO 'file.csv' CSV HEADER; -- Export (Client-side)
\watch 2    -- Re-run query every 2 seconds
\timing     -- Toggle query execution timer
```

### Indexing

```sql
CREATE INDEX idx_user_email ON users(email);              -- Standard B-Tree
CREATE INDEX idx_posts_gin ON posts USING GIN (to_tsvector('english', body)); -- Full-Text Search
CREATE UNIQUE INDEX idx_unique_active_user ON users(email) WHERE role = 'admin'; -- Partial Index
```

### Advanced Postgres

```sql
-- UPSERT
INSERT INTO stats (id, count) VALUES (1, 1)
ON CONFLICT (id) DO UPDATE SET count = stats.count + 1;

-- Window Functions (Calc without collapsing rows)
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- Performance
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@ex.com';
```

---

## 7. Triggers & Functions (PL/pgSQL)

### The Function Part

```sql
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### The Trigger Part

```sql
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_modified_column();
```

### JSONB Manipulation

```sql
SELECT data->>'name' FROM profiles;           -- Get value as text
SELECT data @> '{"role": "admin"}' FROM log;  -- Check if contains key/value
UPDATE profiles SET data = jsonb_set(data, '{city}', '"London"') WHERE id = 1;
```

---

## 8. Glossary & Abbreviations

| Term         | Full Name                             | Description                                                                           |
| :----------- | :------------------------------------ | :------------------------------------------------------------------------------------ |
| **DDL**      | Data Definition Language              | Commands that define the structure (Schema) of the DB (e.g., `CREATE`, `ALTER`).      |
| **DML**      | Data Manipulation Language            | Commands that modify the data within the tables (e.g., `INSERT`, `UPDATE`, `DELETE`). |
| **DQL**      | Data Query Language                   | Commands used to retrieve data (e.g., `SELECT`).                                      |
| **CTE**      | Common Table Expression               | A temporary result set used within a larger query (the `WITH` clause).                |
| **ACID**     | Atomic, Consistent, Isolated, Durable | The 4 key properties of a database transaction.                                       |
| **JSONB**    | JSON Binary                           | An optimized, binary storage format for JSON that supports indexing.                  |
| **GIN**      | Generalized Inverted Index            | An index type for data with multiple values (JSONB, Full-Text Search).                |
| **BRIN**     | Block Range Index                     | An index for very large tables where data is physically ordered by a column.          |
| **PL/pgSQL** | Proc. Language / PostgreSQL           | PostgreSQL's procedural programming language (used for functions/triggers).           |
| **UPSERT**   | Update + Insert                       | An operation that inserts a row or updates it if it already exists (`ON CONFLICT`).   |
