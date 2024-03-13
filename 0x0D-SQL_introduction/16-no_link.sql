-- lists all the records of the second_table of the database hbtn_0c_0 in MySQL server.
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
