# opencart-e2e/tests/account/test_register_negative_invalid_email.py
from selenium.webdriver.common.by import By

from pages.register_page import RegisterPage
from pages.components.header import Header

def test_register_negative_invalid_email(driver, wait):
    page = RegisterPage(driver)
    header = Header(driver)

    # Open homepage
    page.open("https://demo.opencart.com/")

    # Use Header component to navigate
    header.open_register()

    # Fill form with already registered email
    page.fill_form("Test", "One", "testone", "Testone")
    page.agree_privacy()
    page.submit()

    # Capture browser's validation message
    email_field = driver.find_element(By.ID, "input-email")
    validation_msg = email_field.get_attribute("validationMessage")

    print("Browser validation message:", validation_msg)

    # Assert (note: exact wording depends on browser)
    assert "@" in validation_msg, "Expected '@' validation error not shown"