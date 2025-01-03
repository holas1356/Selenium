from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from utils.test_base import LoginPageSelectors 
from utils.browser_utils import wait_for_element
from selenium.common.exceptions import StaleElementReferenceException
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
        self.email_field = LoginPageSelectors.EMAIL_INPUT
        self.password_field = LoginPageSelectors.PASSWORD_INPUT
        self.next_button = LoginPageSelectors.NEXT_BUTTON
        
        self.CODE_NUMBER = (By.XPATH, "//*[@id='idRichContext_DisplaySign']")
 
 
    

    def enter_email(self, email):
        email_field = wait_for_element(self.driver, self.email_field)
        email_field.clear()
        email_field.send_keys(email)

    def click_next(self):
        try:
            next_button = wait_for_element(self.driver, self.next_button, EC.element_to_be_clickable)
            next_button.click()
        except StaleElementReferenceException:
            next_button = wait_for_element(self.driver, self.next_button, EC.element_to_be_clickable)
            next_button.click()

    def enter_password(self, password):
        time.sleep(2)
        password_field = wait_for_element(self.driver, self.password_field)
        password_field.clear() 
        password_field.send_keys(password)
        
    def print_code(self):
        """Print the code number"""
        code_number = wait_for_element(self.driver,self.CODE_NUMBER)
        return code_number.text
    
    def confirm_sign_in(self):
        self.click_next()
       

    def login(self, email, password):
        self.enter_email(email)
        self.click_next()
        self.enter_password(password)
        self.click_next()
        print("Código de autenticación: ", self.print_code())
        self.confirm_sign_in()

        if "Home" in self.driver.title:
            print("Autenticación exitosa y acceso al sistema")
        else:
            print("No se pudo autenticar correctamente")

