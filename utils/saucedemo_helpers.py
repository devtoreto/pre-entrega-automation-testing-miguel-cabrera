import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
TIMEOUT = 15
logger = logging.getLogger(__name__)


def wait_visible(driver, locator):
    return WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located(locator))


def wait_clickable(driver, locator):
    return WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable(locator))


def login(driver):
    driver.get(BASE_URL)
    wait_visible(driver, (By.ID, "user-name")).send_keys(USERNAME)
    wait_visible(driver, (By.ID, "password")).send_keys(PASSWORD)
    wait_clickable(driver, (By.ID, "login-button")).click()
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/inventory.html"))
    logger.info("Login realizado; URL: %s", driver.current_url)


def first_product(driver):
    return wait_visible(driver, (By.CSS_SELECTOR, ".inventory_item"))
