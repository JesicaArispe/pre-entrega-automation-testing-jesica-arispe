from page.login_page import LoginPage
import os
from datetime import datetime

def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    assert login_page.is_login_successful(), "No se redirigió a /inventory.html"
    assert login_page.get_inventory_title() == "Products", "El título no coincide con 'Products'"

    # Captura de pantalla
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join("reports", f"login_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"\nCaptura guardada en: {screenshot_path}")