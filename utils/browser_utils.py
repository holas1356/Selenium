from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def init_driver():
    """Inicializa el WebDriver para Chrome y lo devuelve"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver
