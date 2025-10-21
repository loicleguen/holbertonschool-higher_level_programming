-- 9. Cities by States
-- Script that lists all cities with their state names using a JOIN

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
