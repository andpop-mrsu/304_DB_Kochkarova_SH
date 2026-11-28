-- db_init.sql
-- Лабораторная работа 4: создание и наполнение базы данных movies_rating.db
--
-- ВНИМАНИЕ: раздел ниже между строками-маркерами замените блоком INSERT-строк
-- из вашего db_init.sql, подготовленного в лабораторной работе 2
-- (файл из каталога Task02). Запуск скрипта должен укладываться в 2 секунды.

BEGIN;

DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
    id     INTEGER PRIMARY KEY,
    title  TEXT,
    year   INTEGER,
    genres TEXT
);

CREATE TABLE users (
    id            INTEGER PRIMARY KEY,
    name          TEXT,
    email         TEXT,
    gender        TEXT,
    register_date TEXT,
    occupation    TEXT
);

CREATE TABLE ratings (
    id        INTEGER PRIMARY KEY,
    user_id   INTEGER,
    movie_id  INTEGER,
    rating    REAL,
    timestamp TEXT
);

CREATE TABLE tags (
    id        INTEGER PRIMARY KEY,
    user_id   INTEGER,
    movie_id  INTEGER,
    tag       TEXT,
    timestamp TEXT
);

-- ==================== НАЧАЛО БЛОКА С ДАННЫМИ ====================
-- Сюда вставьте все INSERT-строки из Task02/db_init.sql (л/р 2), например:
-- INSERT INTO movies (id, title, year, genres) VALUES (1, 'Toy Story (1995)', 1995, 'Animation|Children|Comedy');
-- INSERT INTO users (id, name, email, gender, register_date, occupation) VALUES (...);
-- INSERT INTO ratings (id, user_id, movie_id, rating, timestamp) VALUES (...);
-- INSERT INTO tags (id, user_id, movie_id, tag, timestamp) VALUES (...);
-- ==================== КОНЕЦ БЛОКА С ДАННЫМИ =====================

COMMIT;
