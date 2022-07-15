-- WRITE A SCRIPT THAT CREATES A TABLE SECOND_TABLE IN THE DATABASE HBTN_0C_0
-- CREATE AND ADD DATA TO A TABLE
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
