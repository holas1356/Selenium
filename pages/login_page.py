from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_base import LoginPageSelectors 
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
        self.email_field = LoginPageSelectors.EMAIL_INPUT
        self.password_field = LoginPageSelectors.PASSWORD_INPUT
        self.next_button = LoginPageSelectors.NEXT_BUTTON
        self.sign_in_button = LoginPageSelectors.KEEP_SIGNED_BUTTON
        self.keep_signed_in_no_button = LoginPageSelectors.KEEP_SIGNED_BUTTON_NO

    def enter_email(self, email):
        """Introduce el correo electrónico en el campo correspondiente."""
        email_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.email_field)
        )
        email_field.clear()
        email_field.send_keys(email)

    def click_next(self):
        """Hace clic en el botón 'Next' después de ingresar el correo."""
        next_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.next_button)
        )
        next_button.click()

    def enter_password(self, password):
        """Introduce la contraseña y la envía."""
        password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.password_field)
        )
        password_field.clear() 
        password_field.send_keys(password)
    
        sign_in_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.sign_in_button)
        )
        sign_in_button.click()

    def confirm_sign_in(self):
        """Hace clic en el botón 'Keep me signed in'."""
        keep_signed_in_no_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.keep_signed_in_no_button)
            )
        keep_signed_in_no_button.click()
        print("Botón 'No' presionado.")

    def login(self, email, password):
        """Flujo completo de inicio de sesión."""
        self.enter_email(email)
        self.click_next()
        self.enter_password(password)
        self.confirm_sign_in()

        if "Home" in self.driver.title:
            print("Autenticación exitosa y acceso al sistema")
        else:
            print("No se pudo autenticar correctamente")

