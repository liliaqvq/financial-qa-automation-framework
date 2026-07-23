import sqlite3

def setup_mock_bank_db():
    """Inicializa una base de datos relacional para pruebas bancarias."""
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()
    
    # Crear tabla de cuentas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY,
            user_id TEXT,
            balance REAL
        )
    ''')
    
    # Crear tabla de transacciones
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_account INTEGER,
            receiver_account INTEGER,
            amount REAL,
            status TEXT
        )
    ''')
    
    # Insertar datos de prueba
    cursor.execute("INSERT OR REPLACE INTO accounts VALUES (1001, 'user_test', 5000.00)")
    cursor.execute("INSERT OR REPLACE INTO accounts VALUES (2002, 'receiver_test', 1200.00)")
    
    conn.commit()
    conn.close()

def get_account_balance(account_number: int) -> float:
    """Ejecuta una consulta SQL para verificar el saldo actualizado."""
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0.0
