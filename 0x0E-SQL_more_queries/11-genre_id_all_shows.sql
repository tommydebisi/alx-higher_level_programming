-- This script lists all shows contained in the database hbtn_0d_tvshows.

-- Modifying a column by adding constraint
ALTER TABLE tv_show_genres MODIFY tv_show_genres.genre_id INT DEFAULT NULL;

-- Inserting show titles into tv_shows
INSERT INTO tv_shows(title) VALUES('Better Call Saul');
INSERT INTO tv_shows(title) VALUES('Homeland');

-- Inserting show id into tv_show_genres
INSERT INTO tv_show_genres(show_id) VALUES(11);
INSERT INTO tv_show_genres(show_id) VALUES(12);

-- using join to dsplay data and order based on title and genre id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
