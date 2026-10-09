#!/usr/bin/env python3
"""Генератор SQL-скрипта db_init.sql для базы movies_rating.db."""
import csv
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_FILE = os.path.join(HERE, "db_init.sql")


def sql_str(value):
    """Экранирует одиночные кавычки в строке для SQL."""
    if value is None or value == "":
        return "NULL"
    return "'" + str(value).replace("'", "''") + "'"


def parse_title(title):
    """Из 'Toy Story (1995)' вернуть ('Toy Story', 1995)."""
    m = re.search(r"\((\d{4})\)\s*$", title.strip())
    if m:
        return title[:m.start()].strip(), int(m.group(1))
    return title.strip(), None


def main():
    lines = []
    lines.append("PRAGMA foreign_keys = OFF;")
    lines.append("BEGIN TRANSACTION;")

    # Удаляем старые таблицы
    for t in ("ratings", "tags", "movies", "users"):
        lines.append(f"DROP TABLE IF EXISTS {t};")

    # Создаём таблицы
    lines.append("""CREATE TABLE movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        year INTEGER,
        genres TEXT
    );""")

    lines.append("""CREATE TABLE ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        rating REAL NOT NULL,
        timestamp INTEGER NOT NULL
    );""")

    lines.append("""CREATE TABLE tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        tag TEXT,
        timestamp INTEGER NOT NULL
    );""")

    lines.append("""CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        gender TEXT,
        register_date TEXT,
        occupation TEXT
    );""")

    # movies.csv
    with open(os.path.join(HERE, "movies.csv"), encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            title, year = parse_title(row["title"])
            year_sql = str(year) if year is not None else "NULL"
            lines.append(
                f"INSERT INTO movies VALUES "
                f"({row['movieId']}, {sql_str(title)}, {year_sql}, {sql_str(row['genres'])});"
            )

    # ratings.csv
    with open(os.path.join(HERE, "ratings.csv"), encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            lines.append(
                f"INSERT INTO ratings (user_id, movie_id, rating, timestamp) VALUES "
                f"({row['userId']}, {row['movieId']}, {row['rating']}, {row['timestamp']});"
            )

    # tags.csv
    with open(os.path.join(HERE, "tags.csv"), encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            lines.append(
                f"INSERT INTO tags (user_id, movie_id, tag, timestamp) VALUES "
                f"({row['userId']}, {row['movieId']}, {sql_str(row['tag'])}, {row['timestamp']});"
            )

    # users.txt (разделитель "|", без заголовка)
    with open(os.path.join(HERE, "users.txt"), encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("|")
            if len(parts) < 6:
                continue
            uid, name, email, gender, reg_date, occupation = parts[:6]
            lines.append(
                f"INSERT INTO users VALUES "
                f"({uid}, {sql_str(name)}, {sql_str(email)}, {sql_str(gender)}, "
                f"{sql_str(reg_date)}, {sql_str(occupation)});"
            )

    lines.append("COMMIT;")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"OK: {OUT_FILE} ({len(lines)} строк)")


if __name__ == "__main__":
    main()
