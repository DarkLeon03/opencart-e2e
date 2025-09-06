# opencart-e2e/tests/account/test_register_positive.py
import time
from selenium.webdriver.common.by import By
from pages.register_page import RegisterPage
from pages.components.header import Header

def test_register_positive(driver, wait):
    page = RegisterPage(driver)
    header = Header(driver)

    # Open homepage
    page.open("https://demo.opencart.com/")

    # Use Header component to navigate
    header.open_register()

    # Fill valid details (unique email per run)
    unique_email = f"auto{int(time.time())}@example.com"

    # Fill form with already registered email
    page.fill_form("Darkef", "Onefe", unique_email, "Testone")
    page.agree_privacy()
    page.submit()

    # Assert: success heading on the next page
    success_h1 = page.account_created()  # returns text of <div id="content"> <h1>...</h1>
    if "Your Account Has Been Created!" not in success_h1:
        # ---- quick diagnostics if we’re still on form ----
        try:
            print("First name error:", page.get_firstname_error())
            print("Last  name error:", page.get_lastname_error())
            print("Email error    :", page.get_email_error())
            print("Password error :", page.get_password_error())
        except Exception:
            pass
        try:
            print("Top alert:", page.get_alert())  # e.g., “You must agree to the Privacy Policy!”
        except Exception:
            pass
        # Also show whether the checkbox is actually selected
        try:
            agree = driver.find_element(By.NAME, "agree")
            print("Agree selected?:", agree.is_selected())
        except Exception:
            pass

    assert "Your Account Has Been Created!" in success_h1, (
        f"Registration did not succeed. Heading was: {success_h1} (email used: {unique_email})"
    )

    # click Continue to go to Account Dashboard
    page.continue_after_success()

    # you can assert the next page too, e.g. title or heading
    assert "My Account" in driver.title