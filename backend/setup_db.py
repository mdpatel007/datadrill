import sqlite3

conn = sqlite3.connect("datadrill.db")
cursor = conn.cursor()

# Drop tables if already exist (to reset)
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS invoices")

# Create customers table
cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
""")

# Create invoices table
cursor.execute("""
CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    amount REAL,
    date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
""")

# Insert sample data into customers
customers = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com"),
    ("David", "david@example.com")
]
cursor.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", customers)

# Insert sample data into invoices
invoices = [
    (1, 120.50, "2023-01-15"),
    (2, 99.99, "2023-01-18"),
    (1, 300.00, "2023-02-01"),
    (3, 150.75, "2023-02-05"),
    (2, 200.25, "2023-03-10"),
    (4, 350.00, "2023-04-22"),
    (3, 80.00, "2023-05-10")
]
cursor.executemany("INSERT INTO invoices (customer_id, amount, date) VALUES (?, ?, ?)", invoices)

conn.commit()
conn.close()

print("✅ Database created and sample data inserted.")
