import pytest
from src.database import init_mock_database, get_connection

@pytest.fixture(scope="module")
def test_db_path(tmp_path_factory):
    db_file = tmp_path_factory.mktemp("data") / "test_retail.db"
    init_mock_database(str(db_file))
    return str(db_file)

def test_database_tables_exist(test_db_path):
    conn = get_connection(test_db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cur.fetchall()]
    assert "customers" in tables
    assert "orders" in tables
    conn.close()

def test_customer_records_seeded(test_db_path):
    conn = get_connection(test_db_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM customers")
    count = cur.fetchone()[0]
    assert count >= 5
    conn.close()
