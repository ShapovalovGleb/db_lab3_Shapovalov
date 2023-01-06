DO $$
DECLARE
genre_id  genres.genre_id%TYPE;
genre_name genres.genre_name%TYPE;
BEGIN
genre_name := 'Genre';
FOR counter in (SELECT (MAX(genres.genre_id) + 1) FROM genres) .. (SELECT (MAX(genres.genre_id) + 11) FROM genres)
LOOP
INSERT INTO Genres (genre_id, genre_name)
VALUES (counter, genre_name || counter);
END LOOP;
END;
$$

SELECT * FROM genres
DO $$
	BEGIN
		FOR counter in 16..26
		    LOOP
				DELETE FROM genres WHERE genres.genre_id = counter;
			END LOOP;
END;
$$