# tests/account/test_login_logout.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.register_page import RegisterPage
from pages.components.header import Header

def test_login_logout(driver, wait):
    page = RegisterPage(driver)
    header = Header(driver)

    # Go to Login
    page.open("https://demo.opencart.com/")
    header.open_login()

    # Login with valid existing credentials
    page.user_login("darkleon1998@gmail.com", "Darkleon")

    # Verify: My Account page loaded (H1 usually says "My Account")
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div#content h2"), "My Account"))

    # Logout
    header.open_logout()

    # Click on
    logout_success_h1 = page.account_logged_out()    # wait for "Account Logout"
    assert "Account Logout" in logout_success_h1

    # click Continue to go to Account Dashboard
    page.continue_after_success()

    # you can assert the next page too, e.g. title or heading
    assert "Your Store" in driver.title
