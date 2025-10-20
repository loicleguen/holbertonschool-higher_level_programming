-- Convert the database hbtn_0c_0 to UTF8 (utf8mb4) and collation utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- Convert the table first_table to UTF8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert the column 'name' in first_table to UTF8
ALTER TABLE first_table
MODIFY name VARCHAR(256)
