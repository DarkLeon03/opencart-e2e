# pages/register_page.py
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegisterPage(BasePage):
    # Fields
    FIRSTNAME                   = (By.ID, "input-firstname")
    LASTNAME                    = (By.ID, "input-lastname")
    EMAIL                       = (By.ID, "input-email")
    PASSWORD                    = (By.ID, "input-password")

    # Controls
    NEWSLETTER                  = (By.ID, "input-newsletter")
    AGREE                       = (By.NAME, "agree")
    CONTINUE                    = (By.CSS_SELECTOR, "button.btn.btn-primary")
    CONTINUE_AFTER_SUCCESS      = (By.XPATH, "//a[text()='Continue']")

    # Messages
    ALERT                       = (By.CSS_SELECTOR, "#alert .alert")
    SUCCESS_HEADING             = (By.TAG_NAME, "h1")
    ACCOUNT_CREATED             = (By.CSS_SELECTOR, "div[id='content'] h1")
    ACCOUNT_LOGOUT              = (By.CSS_SELECTOR, "div[id='content'] h1")

    # Field error locators
    ERROR_FIRSTNAME             = (By.ID, "error-firstname")
    ERROR_LASTNAME              = (By.ID, "error-lastname")
    ERROR_EMAIL                 = (By.ID, "error-email")
    ERROR_PASSWORD              = (By.ID, "error-password")

    # Login Creds
    EMAIL_ADDRESS               = (By.ID, "input-email")
    PASSWORD_ADDRESS            = (By.ID, "input-password")
    ACCOUNT_LOGIN               = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT                      = (By.XPATH, "//a[@class='list-group-item' and text()='Logout']")

    # Forgotten password
    FORGOTTEN_LINK              = (By.XPATH, "//div[@id='content']//a[text()='Forgotten Password']")
    FORGOTTEN_SUCCESS           = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")  # success banner

    # Actions
    def fill_form(self, firstname, lastname, email, password):
        self.type(self.FIRSTNAME, firstname)
        self.type(self.LASTNAME, lastname)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)

    def toggle_newsletter(self):
        try:
            self.click(self.NEWSLETTER)
        except Exception:
            pass

    def agree_privacy(self):
        el = self.wait.until(EC.presence_of_element_located(self.AGREE))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            self.wait.until(EC.element_to_be_clickable(self.AGREE)).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)
        # verify it actually got checked
        assert el.is_selected(), "Privacy checkbox did not get selected"

    def submit(self):
        btn = self.wait.until(EC.presence_of_element_located(self.CONTINUE))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        try:
            self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", btn)

    # Reads
    def get_alert(self):
        return self.get_text(self.ALERT)

    def get_success(self):
        return self.get_text(self.SUCCESS_HEADING)

    # Error reads with non-empty wait
    def get_firstname_error(self):
        return self.get_text_when_non_empty(self.ERROR_FIRSTNAME)

    def get_lastname_error(self):
        return self.get_text_when_non_empty(self.ERROR_LASTNAME)

    def get_email_error(self):
        return self.get_text_when_non_empty(self.ERROR_EMAIL)

    def get_password_error(self):
        return self.get_text_when_non_empty(self.ERROR_PASSWORD)

    # Your Account Has Been Created!
    def account_created(self):
        # wait until the success heading is present on the page
        self.wait.until(EC.text_to_be_present_in_element(self.ACCOUNT_CREATED, "Your Account Has Been Created!"))
        return self.get_text(self.ACCOUNT_CREATED)

    def continue_after_success(self):
        self.click(self.CONTINUE_AFTER_SUCCESS)

    def user_login(self, email_address, password_address):
        self.type(self.EMAIL_ADDRESS, email_address)
        self.type(self.PASSWORD_ADDRESS, password_address)
        self.click(self.ACCOUNT_LOGIN)

    def logout(self):
        self.click(self.LOGOUT)

    def account_logged_out(self):
        self.wait.until(EC.text_to_be_present_in_element(self.ACCOUNT_LOGOUT, "Account Logout"))
        return self.get_text(self.ACCOUNT_LOGOUT)

    def open_forgotten_password(self):
        self.click(self.FORGOTTEN_LINK)

    def request_password_reset(self, email_address):
        self.type(self.EMAIL_ADDRESS, email_address)
        self.click(self.CONTINUE)

    def get_forgotten_success(self):
        # wait until success banner has non-empty text
        return self.get_text_when_non_empty(self.FORGOTTEN_SUCCESS)



