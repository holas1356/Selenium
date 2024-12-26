from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_base import LogisticsPageSelectors
from utils.browser_utils import wait_for_element
import os

class LogisticsPage:
    def __init__(self, driver):
        self.driver = driver

        self.logistics_icon_locator = LogisticsPageSelectors.LOGISTICS_ICON_LOCATOR
        self.inventory_master_option_locator = LogisticsPageSelectors.INVENTORY_MASTER_OPTION_LOCATOR
        
    def go_to_logistics_page(self):
        logistics_icon = wait_for_element(self.driver, self.logistics_icon_locator, EC.visibility_of_element_located)
        actions = ActionChains(self.driver)
        actions.move_to_element(logistics_icon).perform()


        inventory_master_option = wait_for_element(self.driver, self.inventory_master_option_locator, EC.element_to_be_clickable)
        inventory_master_option.click()
        
    def verify_inventory_master_page(self):
        inventory_url = os.getenv("INVENTORY_URL")
        expected_url = inventory_url
        wait_for_element(self.driver, expected_url, EC.url_to_be)
        assert self.driver.current_url == expected_url, f"Expected {expected_url} but got {self.driver.current_url}"