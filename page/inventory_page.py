from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
#Representa la página de inventario (catálogo de productos).

    _PAGE_TITLE = (By.CSS_SELECTOR, "div.header_secondary_container .title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _FILTER = (By.CLASS_NAME, "product_sort_container")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
#Obtiene el texto del título de la página.
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._PAGE_TITLE)
        ).text

    def get_product_count(self):
#Cuenta cuántos productos hay visibles.
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._PRODUCTS)
        )
        return len(self.driver.find_elements(*self._PRODUCTS))

    def interface_elements_visible(self):
#Valida que menú y filtro estén presentes.
        menu = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self._MENU_BUTTON)
        )
        filtro = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self._FILTER)
        )
        return menu.is_displayed() and filtro.is_displayed()
    
    def get_first_product_info(self):
#Obtiene el nombre y precio del primer producto visible.
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self._PRODUCTS)
            )
            first_name = self.driver.find_elements(*self._PRODUCT_NAME)[0].text
            first_price = self.driver.find_elements(*self._PRODUCT_PRICE)[0].text
            return first_name, first_price