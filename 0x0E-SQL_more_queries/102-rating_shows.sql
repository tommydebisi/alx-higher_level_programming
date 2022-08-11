-- This script lists all shows from hbtn_0d_tvshows_rate by their rating

-- Use of inner join
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
FULL OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
FULL OUTER JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
