'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 13 Assignment 4
Code Helper - Gemini Google AI
'''

import sqlite3

# 1. Setup Connection and Table
conn = sqlite3.connect('business_data.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Products') # Reset for clean run
cursor.execute('''
    CREATE TABLE Products (
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL,
        stock INTEGER
    )
''')

# 2. Insert Data
products_to_add = [
    (1, 'Widget', 10.5, 100),
    (2, 'Gadget', 15.0, 50),
    (3, 'Doohickey', 12.5, 75)
]
cursor.executemany('INSERT INTO Products VALUES (?, ?, ?, ?)', products_to_add)
conn.commit()

# 3. Query: Products with price > 11.0
print("Products with price > 11.0:")
cursor.execute('SELECT * FROM Products WHERE price > 11.0')
rows = cursor.fetchall()
for row in rows:
    print(row)

# 4. Update: Reduce stock for 'Widget' by 10
cursor.execute("UPDATE Products SET stock = stock - 10 WHERE name = 'Widget'")
conn.commit()

# 5. Final Print to match sample
print("\nUpdated Widget Stock:")
cursor.execute("SELECT name, stock FROM Products WHERE name = 'Widget'")
print(cursor.fetchone())

conn.close()

