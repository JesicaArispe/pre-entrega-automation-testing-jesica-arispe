import pytest
from utils.helpers import get_driver

@pytest.fixture
def driver():
    #Fixture que abre y cierra el navegador para cada test.
    driver = get_driver()
    yield driver
    driver.quit()