from page.login_page import LoginPage
from page.inventory_page import InventoryPage

def test_catalogo_productos(driver):
#Verifica el título, los productos y elementos del catálogo.
    # Paso 1: Login para llegar al inventario
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    # Paso 2: Crear instancia de InventoryPage
    inventario = InventoryPage(driver)

    # Verificar título
    assert inventario.get_page_title() == "Products", "El título del inventario no es correcto."

    # Verificar que haya al menos un producto visible
    assert inventario.get_product_count() > 0, "No se encontraron productos visibles."

    # Validar que elementos importantes estén presentes
    assert inventario.interface_elements_visible(), "El menú o los filtros no están visibles."

    #Listar nombre y precio del primer producto
    name, price = inventario.get_first_product_info()
    print(f"\nPrimer producto visible: {name} - {price}")
    assert name != "" and price != "", "No se pudo obtener nombre o precio del primer producto."