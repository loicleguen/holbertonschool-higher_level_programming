-- 3. Always a name
-- Script that creates the table force_name on the MySQL server with id and name (not null)

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
