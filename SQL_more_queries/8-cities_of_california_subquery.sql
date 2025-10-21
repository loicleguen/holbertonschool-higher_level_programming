-- 8. Cities of California
-- Script that lists all cities of California using a subquery (no JOIN)

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
