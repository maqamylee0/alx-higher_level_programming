-- lists all the cities of California

SELECT id, name
FROM cities
WHERE state_id = (
	SELECT states.id
	FROM states
	WHERE states.name = 'California'
);
