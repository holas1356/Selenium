from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.test_base import ImportPageSelectors
from utils.browser_utils import wait_for_element
import os

class ImportPage:
    def __init__(self, driver):
        self.driver = driver

        self.system_icon_locator = ImportPageSelectors.SYSTEM_ICON_LOCATOR
        self.import_option_locator = ImportPageSelectors.IMPORT_OPTION_LOCATOR
        self.import_dropdown_locator = ImportPageSelectors.IMPORT_DROPDOWN_LOCATOR
        self.file_input_locator = ImportPageSelectors.FILE_INPUT_LOCATOR


    def go_to_import_page(self):
        system_icon = wait_for_element(self.driver, self.system_icon_locator, EC.visibility_of_element_located)
        actions = ActionChains(self.driver)
        actions.move_to_element(system_icon).perform()


        import_option = wait_for_element(self.driver, self.import_option_locator, EC.element_to_be_clickable)
        import_option.click()

    def verify_import_page(self):
        import_url = os.getenv("IMPORTS_URL")
        wait_for_element(self.driver, import_url, EC.url_to_be)
        assert self.driver.current_url == import_url, f"Expected {import_url} but got {self.driver.current_url}"
        
    def select_garmy_option(self):
        import_dropdown = wait_for_element(self.driver, self.import_dropdown_locator, EC.visibility_of_element_located)
        dropdown = Select(import_dropdown)
        dropdown.select_by_value("GARMY")

        selected_option = dropdown.first_selected_option
        assert selected_option.text == "GARMY Import", f"Expected 'GARMY Import', but got '{selected_option.text}'"
        
    def upload_csv_file(self, file_path):
        abs_file_path = os.path.abspath(file_path)

        assert os.path.exists(abs_file_path), f"El archivo no existe: {abs_file_path}"

        file_input = wait_for_element(self.driver, self.file_input_locator, EC.presence_of_element_located)
        file_input.send_keys(abs_file_path)

        print(f"Archivo cargado exitosamente: {abs_file_path}")

        
