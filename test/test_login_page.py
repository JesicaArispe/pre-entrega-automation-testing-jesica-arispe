from page.login_page import LoginPage

def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    assert login_page.is_login_successful(), "No se redirigió a /inventory.html"
    assert login_page.get_inventory_title() == "Products", "El título no coincide con 'Products'"