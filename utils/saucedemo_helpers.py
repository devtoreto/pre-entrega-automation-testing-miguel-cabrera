import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
TIMEOUT = 15
logger = logging.getLogger(__name__)


def wait_visible(driver, locator):
    """Espera explícitamente hasta que el elemento sea visible."""
    return WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located(locator))


def wait_clickable(driver, locator):
    """Espera explícitamente hasta que el elemento pueda pulsarse."""
    return WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable(locator))


def pause(driver):
    """Pausa opcional para observar pasos con el navegador visible."""
    seconds = getattr(driver, "step_delay", 0)
    if seconds:
        time.sleep(seconds)


def login(driver):
    """Accede al sitio e inicia sesión con las credenciales de prueba."""
    driver.get(BASE_URL)
    wait_visible(driver, (By.ID, "user-name")).send_keys(USERNAME)
    pause(driver)
    wait_visible(driver, (By.ID, "password")).send_keys(PASSWORD)
    pause(driver)
    wait_clickable(driver, (By.ID, "login-button")).click()
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/inventory.html"))
    logger.info("Login realizado; URL: %s", driver.current_url)
    pause(driver)


def first_product(driver):
    """Devuelve el primer producto visible del inventario."""
    return wait_visible(driver, (By.CSS_SELECTOR, ".inventory_item"))