from pages.register_page import RegisterPage
from pages.components.header import Header

def test_forgotten_password(driver):
    page = RegisterPage(driver)
    header = Header(driver)

    page.open("https://demo.opencart.com")
    header.open_login()
    page.open_forgotten_password()
    page.request_password_reset("darkleon1998@gmail.com")
    msg = page.get_forgotten_success()
    text = msg.lower()
    assert text.startswith("success:") and ("sent" in text or "updated" in text)
