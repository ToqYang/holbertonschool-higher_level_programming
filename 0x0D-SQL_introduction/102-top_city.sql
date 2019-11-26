-- Show the top 3 cities more hot
SELECT city, AVG(value) avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city DESC
ORDER BY avg_temp DESC
LIMIT 3;
