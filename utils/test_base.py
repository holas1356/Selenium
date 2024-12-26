"""
Global variables and selectors for ARRO tests.
"""
from selenium.webdriver.common.by import By

URL = "https://isf-arro-qa-logstat.azurewebsites.net/"


class LoginPageSelectors:
    EMAIL_INPUT = (By.ID, "i0116")
    NEXT_BUTTON = (By.ID, "idSIButton9")
    PASSWORD_INPUT = (By.NAME, "passwd")
    
class ImportPageSelectors:
    SYSTEM_ICON_LOCATOR = (By.CSS_SELECTOR, 'li > div.app-menu-system-group-div > p')
    IMPORT_OPTION_LOCATOR = (By.XPATH, "//ul[@class='arro_navbar']/li[6]/div[1]/ul//a[contains(@href,'/Import')]//span[.='Import']")
    IMPORT_DROPDOWN_LOCATOR = (By.ID, "importDropdown")
    FILE_INPUT_LOCATOR = (By.ID, "file-input")
    
class LogisticsPageSelectors:
    LOGISTICS_ICON_LOCATOR = (By.CSS_SELECTOR, 'li > div.app-menu-logistics-group-div > p')
    INVENTORY_MASTER_OPTION_LOCATOR = (By.XPATH, "//ul[@class='arro_navbar']/li[4]/div[1]/ul//a[@href='https://isf-arro-qa-logstat.azurewebsites.net/InventoryMaster']//span[.='Inventory Master']")
    

