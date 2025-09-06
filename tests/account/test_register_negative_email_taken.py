# opencart-e2e/tests/account/test_register_negative_email_taken.py
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
    page.fill_form("Test", "One", "testone@gmail.com", "Testone")
    page.agree_privacy()
    page.submit()

    # Assert warning toast
    msg = page.get_alert()
    assert "E-Mail Address is already registered" in msg
