from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ImportPage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores para interactuar con el dropdown de 'System' y la opción 'Import'
        self.system_icon_locator = (By.CSS_SELECTOR, 'li > div.app-menu-system-group-div > p')  # Icono 'System'
        self.import_option_locator = (By.XPATH, "//a[contains(text(), 'Import')]")  # Opción 'Import' en el dropdown
        self.dropdown_locator = (By.CSS_SELECTOR, 'div.arro_navbar_popover')  # El contenedor del dropdown

    def go_to_import_page(self):
        # Espera a que el ícono de 'System' esté visible y haz clic en él para mostrar el dropdown
        system_icon = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.system_icon_locator)
        )

        # Mover el mouse sobre el ícono para que se despliegue el menú
        actions = ActionChains(self.driver)
        actions.move_to_element(system_icon).perform()

        # Espera a que el dropdown sea visible (el contenedor donde están las opciones del menú)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.dropdown_locator)
        )

        # Espera a que la opción 'Import' sea visible y haz clic en ella
        import_option = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.import_option_locator)
        )
        import_option.click()

    def verify_import_page(self):
        # Verifica que la URL sea la esperada después de hacer clic en 'Import'
        expected_url = "https://isf-arro-qa-logstat.azurewebsites.net/Import"
        WebDriverWait(self.driver, 60).until(
            EC.url_to_be(expected_url)
        )
        assert self.driver.current_url == expected_url, f"Expected {expected_url} but got {self.driver.current_url}"
