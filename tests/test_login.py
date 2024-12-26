import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.import_page import ImportPage
from pages.logistics_page import LogisticsPage
from utils.browser_utils import init_driver
import os
import time
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="function")
def setup():
    driver = init_driver()

    base_url = os.getenv("BASE_URL")
    driver.get(base_url)
    
    yield driver
    driver.quit()

def test_login_successful(setup):
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    login_page = LoginPage(setup)
    login_page.login(email, password)
    assert "Home" in setup.title, "La autenticación no fue exitosa. Título encontrado: " + setup.title
    import_page = ImportPage(setup)
    import_page.go_to_import_page()
    import_page.verify_import_page()
    import_page.select_garmy_option()

    import_page.upload_csv_file("tests/documents/test_GARMY_Luisa_3.csv")
    time.sleep(30)
    assert "Imports" in setup.title, "La autenticación no fue exitosa. Título encontrado: " + setup.title
    logistics_page = LogisticsPage(setup)
    logistics_page.go_to_logistics_page()
    logistics_page.verify_inventory_master_page()
    logistics_page.select_tactical_type()
    logistics_page.enter_nomenclature("Test")
    time.sleep(20)
    assert "Inventory" in setup.title, "La autenticación no fue exitosa. Título encontrado: " + setup.title
    
   
