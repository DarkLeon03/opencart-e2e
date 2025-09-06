# opencart-e2e/tests/account/test_register_negative_weak_password.py
from pages.register_page import RegisterPage
from pages.components.header import Header

def test_register_negative_already_registered_email(driver, wait):
    page = RegisterPage(driver)
    header = Header(driver)

    # Open homepage
    page.open("https://demo.opencart.com/")

    # Use Header component to navigate
    header.open_register()

    # Fill form with already registered email
    page.fill_form("Testcase", "one", "testcaseone@gmail.com", "123")
    page.agree_privacy()
    page.submit()

    # Assertions for all fields errors
    assert "Password must be between 4 and 20 characters!"   in page.get_password_error()

