-- Show State
SELECT state, MAX(value) max_temp
FROM temperatures
GROUP BY state
LIMIT 3;
