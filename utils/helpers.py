from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
import time

# Datos del sitio y credenciales
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def get_driver():
#Inicializa el navegador Chrome y lo devuelve listo para usar.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    #time.sleep(5)
    driver.implicitly_wait(5)
    driver.maximize_window()
    
    return driver

