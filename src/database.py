import sqlite3
from src.config import DB_PATH

def get_connection(db_path: str = DB_PATH):
    return sqlite3.connect(db_path)

def init_mock_database(db_path: str = DB_PATH):
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            tier TEXT NOT NULL,
            region TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)
    cur.execute("SELECT COUNT(*) FROM customers")
    if cur.fetchone()[0] == 0:
        customers = [
            (1, 'Apex Logistics', 'Enterprise', 'North America'),
            (2, 'Nexus Tech', 'Pro', 'Europe'),
            (3, 'Global Health Corp', 'Enterprise', 'APAC'),
            (4, 'Zenith Retailers', 'Standard', 'North America'),
            (5, 'BlueWave Software', 'Pro', 'Europe')
        ]
        orders = [
            (101, 1, 12500.00, 'Completed', '2025-01-15'),
            (102, 1, 6200.00, 'Completed', '2025-02-10'),
            (103, 2, 3400.00, 'Pending', '2025-02-18'),
            (104, 3, 28000.00, 'Completed', '2025-03-01'),
            (105, 4, 850.00, 'Refunded', '2025-03-05'),
            (106, 5, 4100.00, 'Completed', '2025-03-12')
        ]
        cur.executemany("INSERT INTO customers VALUES (?,?,?,?)", customers)
        cur.executemany("INSERT INTO orders VALUES (?,?,?,?,?)", orders)
        conn.commit()
    conn.close()

if __name__ == "__main__":
    init_mock_database()
