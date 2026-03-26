import sqlite3

connect = sqlite3.connect("cinema.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
""")

cursor.executemany("""
INSERT INTO users (name) VALUES (?)
""", [
    ("Satoru",),
    ("Itachi",),
    ("Mao Mao",),
    ("Friren",),
    ("Wangji",)
])

cursor.executemany("""
INSERT INTO movies (title, genre) VALUES (?, ?)
""", [
    ("Девочка, покорившая время", "Sci-Fi"),
    ("Эхо террора", "Drama"),
    ("Клинок, рассекающий демонов", "Action"),
    ("Магическая битва", "Action"),
    ("Ванпачмен", "Action")
])

cursor.executemany("""
INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)
""", [
    (1, 1, 9),
    (2, 1, 8),
    (3, 2, 10),
    (4, 2, 9),
    (5, 3, 7),
    (1, 3, 8),
    (2, 4, 9),
    (3, 5, 10),
    (4, 5, 8),
    (5, 4, 7),
    (1, 5, 9)
])

connect.commit()

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
SELECT AVG(rating) FROM reviews
""")
print("Средняя оценка:", cursor.fetchone()[0])

cursor.execute("""
SELECT MAX(rating) FROM reviews
""")
print("Максимальная оценка:", cursor.fetchone()[0])

cursor.execute("""
SELECT MIN(rating) FROM reviews
""")
print("Минимальная оценка:", cursor.fetchone()[0])