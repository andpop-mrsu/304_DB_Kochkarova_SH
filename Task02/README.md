# Task02 — ETL для SQLite

## Назначение

Скрипт `db_init.bat` создаёт базу данных `movies_rating.db` с таблицами
`movies`, `ratings`, `tags`, `users` и наполняет её данными из CSV/TXT-файлов.

## Требования к окружению

- **Python 3** (версия 3.6 или выше)
- **SQLite 3** (команда `sqlite3` должна быть доступна в PATH)
- **Bash** (Linux/macOS — из коробки; Windows — Git Bash или WSL)

## Запуск

```bash
bash db_init.bat
