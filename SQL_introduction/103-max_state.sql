-- Display the max temperature of each state(ordered by State name)
SELECT state, MAX(value) AS max_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY state
ORDER BY state ASC;