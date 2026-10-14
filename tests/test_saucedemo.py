"""Pruebas funcionales independientes para SauceDemo."""
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.saucedemo_helpers import login, wait_visible, wait_clickable, first_product, pause, TIMEOUT
from tests.conftest import screenshot_ok

logger = logging.getLogger(__name__)


def test_login_exitoso(driver):
    """Verifica redirección a inventario y encabezado de la aplicación."""
    login(driver)
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    assert wait_visible(driver, (By.CSS_SELECTOR, ".app_logo")).text == "Swag Labs"
    assert wait_visible(driver, (By.CSS_SELECTOR, ".title")).text == "Products"
    screenshot_ok(driver, "test_login_exitoso")


def test_catalogo_productos(driver):
    """Valida catálogo, controles y registra el primer nombre y precio."""
    login(driver)
    assert wait_visible(driver, (By.CSS_SELECTOR, ".title")).text == "Products"
    assert driver.find_elements(By.CSS_SELECTOR, ".inventory_item"), "No hay productos en el catálogo"
    assert wait_visible(driver, (By.ID, "react-burger-menu-btn")).is_displayed(), "Falta menú"
    assert wait_visible(driver, (By.CSS_SELECTOR, ".product_sort_container")).is_displayed(), "Falta filtro"
    product = first_product(driver)
    name = product.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    price = product.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    assert name.strip(), "Nombre del producto vacío"
    assert price.startswith("$") and len(price) > 1, "Precio inválido"
    logger.info("Primer producto: %s | Precio: %s", name, price)
    print(f"Primer producto: {name} | Precio: {price}")
    screenshot_ok(driver, "test_catalogo_productos")


def test_agregar_producto_carrito(driver):
    """Añade el primer producto y comprueba contador y carrito."""
    login(driver)
    product = first_product(driver)
    name = product.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    pause(driver)
    product.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
    badge = wait_visible(driver, (By.CSS_SELECTOR, ".shopping_cart_badge"))
    assert badge.text == "1", f"Contador inesperado: {badge.text}"
    screenshot_ok(driver, "carrito_01_producto_agregado")
    pause(driver)
    wait_clickable(driver, (By.CSS_SELECTOR, ".shopping_cart_link")).click()
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/cart.html"))
    cart_names = [element.text for element in driver.find_elements(By.CSS_SELECTOR, ".cart_item .inventory_item_name")]
    assert name in cart_names, f"El producto {name!r} no aparece en el carrito: {cart_names}"
    screenshot_ok(driver, "carrito_02_producto_verificado")
    pause(driver)
    logger.info("Producto agregado y verificado en carrito: %s", name)