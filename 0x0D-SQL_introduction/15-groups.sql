-- LISTS THE NUMBER OF RECORDS WITH THE SAME SCORE IN THE TABLE SECOND_TABLE
-- COMMAND TO LIST THE RECORDS WITH THE SAME SCORE
SELECT score, COUNT(*) 'number' FROM second_table GROUP BY score ORDER BY number DESC;