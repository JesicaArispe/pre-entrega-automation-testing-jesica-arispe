from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
#Representa la página del carrito de compras.

    _ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".inventory_item button")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    _CART_ITEM = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver

    def add_first_product(self):
#Agrega el primer producto al carrito.
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._ADD_TO_CART_BTN)
        ).click()

    def get_cart_count(self):
#Devuelve el número del contador del carrito.
        badge = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._CART_BADGE)
        )
        return badge.text

    def open_cart(self):
#Abre el carrito de compras.
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._CART_ICON)
        ).click()

    def is_product_in_cart(self):
#Verifica que el producto agregado esté presente en el carrito.
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._CART_ITEM)
        )
        items = self.driver.find_elements(*self._CART_ITEM)
        return len(items) > 0