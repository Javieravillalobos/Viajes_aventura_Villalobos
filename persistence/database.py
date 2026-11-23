import os
import sqlite3
from pathlib import Path


def get_db_path() -> str:
    """Read DB_PATH from environment or .env file in project root."""
    env_path = os.getenv("DB_PATH")
    if env_path:
        return env_path

    dotenv_file = Path(__file__).resolve().parent.parent / ".env"
    if dotenv_file.exists():
        for line in dotenv_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                if key.strip() == "DB_PATH":
                    return value.strip().strip('"').strip("'")

    return "viajes_aventura.db"


def get_connection() -> sqlite3.Connection:
    """Create and return a SQLite connection."""
    db_path = get_db_path()
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection


def test_connection() -> bool:
    """Run a repeatable connection check against SQLite."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT sqlite_version();")
            version = cursor.fetchone()
            print(f"Conexión exitosa a SQLite (versión: {version[0]}).")
            return True
    except sqlite3.Error as exc:
        print(f"Error al conectar con SQLite: {exc}")
        return False


if __name__ == "__main__":
    test_connection()