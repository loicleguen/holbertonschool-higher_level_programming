SELECT city ROUND(AVG(value, 4)) AS averagetemp
FROM temperature
GROUP BY city
ORDER BY averagetemp desc
