import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.import_page import ImportPage
import time
import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

@pytest.fixture(scope="function")
def setup():
    """Inicializar el navegador para cada test"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Acceder a la URL desde las variables de entorno
    base_url = os.getenv("BASE_URL")
    driver.get(base_url)
    
    yield driver
    driver.quit()

def test_login_successful(setup):
    """Test para realizar login exitoso"""
    # Obtener las credenciales desde el archivo .env
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    
    login_page = LoginPage(setup)
    login_page.login(email, password)
    
    # Espera 10 segundos para que el login se complete
    time.sleep(10)
    import_page = ImportPage(setup)
    import_page.go_to_import_page()
    import_page.verify_import_page()
    
    # Verificar si el login fue exitoso basándonos en el título de la página
    assert "Home" in setup.title, "La autenticación no fue exitosa. Título encontrado: " + setup.title
