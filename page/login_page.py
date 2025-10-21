from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL, USERNAME, PASSWORD

class LoginPage:
#Representa la página de login de saucedemo.com.

    _INPUT_NAME = (By.NAME, "user-name")
    _INPUT_PASSWORD = (By.NAME, "password")
    _LOGIN_BUTTON = (By.NAME, "login-button")
    _PAGE_TITLE = (By.CSS_SELECTOR, "div.header_secondary_container .title")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
#Abre la página de login.
        self.driver.get(URL)

    def login(self, username=USERNAME, password=PASSWORD):
#Realiza el proceso de login con esperas explícitas.
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._INPUT_NAME)).send_keys(username)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._INPUT_PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()

    def is_login_successful(self):
#Valida que la redirección al inventario sea exitosa.
        WebDriverWait(self.driver, 5).until(EC.url_contains("/inventory.html"))
        return "/inventory.html" in self.driver.current_url

    def get_inventory_title(self):
#Obtiene el título de la página de inventario."""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self._PAGE_TITLE)).text