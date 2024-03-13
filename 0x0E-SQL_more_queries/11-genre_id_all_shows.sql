-- script that lists all shows contained in the database hbtn_0d_tvshows.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in the ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show do not have a genre, display NULL
-- You can use only one SELECT statement
-- The database name will be passed as an argument of mysql command

SELECT s.title, g.genre_id
  FROM tv_shows AS s
       LEFT JOIN tv_show_genres AS g
       ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
