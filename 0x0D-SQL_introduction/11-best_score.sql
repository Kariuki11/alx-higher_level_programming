-- list all the records with score >= 10 in the second_table of database hbtn_0c_0 in mysql server
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
