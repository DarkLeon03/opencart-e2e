# opencart-e2e/pages/components/header.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Header(BasePage):
    # Locators
    MY_ACCOUNT  = (By.XPATH, "//span[text()='My Account']")
    REGISTER    = (By.XPATH, "//a[text()='Register']")
    LOGIN       = (By.XPATH, "//a[text()='Login']")
    LOGOUT      = (By.XPATH, "//a[text()='Logout']")
    CONTINUE    = (By.XPATH, "//a[text()='Continue']")  # after logout success


    # Actions
    def open_register(self):
        self.click(self.MY_ACCOUNT)
        self.click(self.REGISTER)

    def open_login(self):
        self.click(self.MY_ACCOUNT)
        self.click(self.LOGIN)

    def open_logout(self):
        self.click(self.MY_ACCOUNT)
        self.click(self.LOGOUT)
        # On the "Account Logout" page there is a Continue link
        #self.click(self.CONTINUE)
