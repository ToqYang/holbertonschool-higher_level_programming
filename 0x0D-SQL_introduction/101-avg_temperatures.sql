-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) avg_temp
FROM temperatures
GROUP BY city DESC
ORDER BY avg_temp DESC;
