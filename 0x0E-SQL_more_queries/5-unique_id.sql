-- Make a table (id, name) Initializes (1 and UNIQ values)
CREATE TABLE IF NOT EXISTS unique_id ( id INT DEFAULT 1 UNIQUE, name VARCHAR(256) );
