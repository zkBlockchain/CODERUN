WITH RECURSIVE track_genres AS (
  SELECT
    t.id AS track_id,
    g.id AS genre_id,
    t.name AS track_name,
    g.name AS genre_name,
    g.parent_genre_id
  FROM
    track AS t
    JOIN track_genre AS tg ON t.id = tg.track_id
    JOIN genre AS g ON tg.genre_id = g.id
  UNION ALL
  SELECT
    tg.track_id,
    g.id,
    tg.track_name,
    g.name,
    g.parent_genre_id
  FROM
    track_genres AS tg
    JOIN genre AS g ON tg.parent_genre_id = g.id
)
SELECT DISTINCT
  track_id,
  genre_id,
  track_name,
  genre_name
FROM
  track_genres
ORDER BY
  track_id,
  genre_id;


