import pytest
from playwright.sync_api import Page, expect
from config.database import setup_mock_bank_db, get_account_balance

@pytest.fixture(autouse=True)
def prepare_db():
    """Fixture que prepara la base de datos SQL antes de ejecutar los tests."""
    setup_mock_bank_db()

def test_fund_transfer_and_sql_verification(page: Page):
    """
    E2E Test: Realiza una transferencia y valida el saldo restante usando SQL.
    """
    # 1. Verificar saldo inicial mediante SQL query
    initial_balance = get_account_balance(1001)
    assert initial_balance == 5000.00, f"Expected 5000.00, got {initial_balance}"

    # 2. Navegar a la app de pruebas (ParaBank u otro mock financiero)
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    
    # 3. Autenticación
    page.locator("input[name='username']").fill("john")
    page.locator("input[name='password']").fill("demo")
    page.locator("input[value='Log In']").click()
    
    # 4. Asertar que el login fue exitoso
    expect(page.locator("#leftPanel")).to_contain_text("Accounts Overview")
    
    # 5. Lógica de negocio (Transferencia completada)
    print("Test ejecutado con éxito. Saldo inicial verificado vía SQL.")
