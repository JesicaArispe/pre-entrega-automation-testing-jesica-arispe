from page.login_page import LoginPage
from page.cart_page import CartPage
import os
from datetime import datetime

def test_agregar_producto_al_carrito(driver):
#Verifica la funcionalidad del carrito de compras.
    # Paso 1: Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    # Paso 2: Crear instancia del carrito
    carrito = CartPage(driver)

    # Agregar el primer producto
    carrito.add_first_product()

    # Verificar que el contador se incremente a 1
    assert carrito.get_cart_count() == "1", "El contador del carrito no se actualizó correctamente."

    # Navegar al carrito
    carrito.open_cart()

    # Verificar que el producto esté en el carrito
    assert carrito.is_product_in_cart(), "El producto no aparece en el carrito."


     # Captura de pantalla (evidencia)
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join("reports", f"carrito_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"\nCaptura guardada en: {screenshot_path}")