import logging
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

ROOT = Path(__file__).resolve().parents[1]
SCREENSHOTS = ROOT / "reports" / "screenshots"
LOGS = ROOT / "reports" / "logs"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--headed", action="store_true", help="Mostrar ventana del navegador")


def pytest_configure(config):
    LOGS.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=LOGS / "execution.log", level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s", force=True)


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")
    if browser == "firefox":
        options = FirefoxOptions()
        if not headed:
            options.add_argument("-headless")
        instance = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,900")
        instance = webdriver.Chrome(options=options)
    instance.set_window_size(1440, 900)
    request.node._driver = instance
    yield instance
    instance.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        logging.error("Fallo en %s (%s): %s", item.nodeid, report.when, report.longreprtext)
        driver = getattr(item, "_driver", None)
        if driver is not None:
            name = "_".join(c if c.isalnum() or c in "-_" else "_" for c in item.nodeid)
            path = SCREENSHOTS / f"{name}_{report.when}.png"
            try:
                driver.save_screenshot(str(path))
                logging.info("Captura guardada: %s", path)
            except Exception:
                logging.exception("No fue posible guardar la captura")
