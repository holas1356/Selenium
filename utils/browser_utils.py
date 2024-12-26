from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

def init_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver



def wait_for_element(driver, locator, condition=EC.presence_of_element_located, timeout=30):
    """Esperar hasta que un elemento cumpla la condición especificada"""
    for _ in range(3):
        try:
            return WebDriverWait(driver, timeout).until(condition(locator))
        except StaleElementReferenceException:
            time.sleep(1) 
    raise Exception(f"Elemento no encontrado o inestable: {locator}")

