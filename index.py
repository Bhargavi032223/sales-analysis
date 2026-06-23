import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price INTEGER
)
""")

cursor.execute("DELETE FROM sales")

sales_data = [
    ('Laptop', 5, 50000),
    ('Mobile', 10, 20000),
    ('Headphones', 20, 2000),
    ('Laptop', 3, 50000),
    ('Mobile', 7, 20000)
]

cursor.executemany(
    "INSERT INTO sales(product, quantity, price) VALUES(?,?,?)",
    sales_data
)

query = """
SELECT product,
SUM(quantity) AS total_quantity,
SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()