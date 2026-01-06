import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
""")

cur.execute("""
INSERT INTO users (name)
SELECT 'Anil'
WHERE NOT EXISTS (SELECT 1 FROM users WHERE name='Anil');
""")

conn.commit()
cur.close()
conn.close()

print("Database migration completed")
