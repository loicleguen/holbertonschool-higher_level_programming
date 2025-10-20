-- Create table second_table and add multiple rows, removing old data if any
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Delete all existing rows to avoid duplicates
DELETE FROM second_table;

-- Insert the required rows
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
