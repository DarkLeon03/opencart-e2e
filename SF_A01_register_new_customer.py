import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


def open_homepage(driver, wait):
    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    # wait until the search bar is present (more reliable than title, avoids Cloudflare issue)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='search']")))
    assert "Store" in driver.title, "Homepage did not load correctly (title mismatch)"
    print(f"[OK] Home title: {driver.title}")

def go_to_register(driver, wait):
    # Click on My Account -> Register
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()= 'My Account']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'dropdown']//a[text()='Register']"))).click()

    # Wait until registration form loads
    firstname = wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    assert firstname.is_displayed(), "Registration form did not load"
    print("[OK] Registration form visible")


def register_user(driver, wait, firstname, lastname, email, password):
    # Enter your personal Details
    driver.find_element(By.ID, "input-firstname").send_keys(firstname)
    driver.find_element(By.ID, "input-lastname").send_keys(lastname)

    # Use an email that is ALREADY REGISTERED
    driver.find_element(By.ID, "input-email").send_keys(email)

    # Enter your password
    driver.find_element(By.ID, "input-password").send_keys(password)

    # (Optional) newsletter – if present
    try:
        driver.find_element(By.ID, "input-newsletter").click()
    except:
        pass

    # Agree to Privacy Policy
    privacy = wait.until(EC.element_to_be_clickable((By.NAME, "agree")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", privacy)
    try:
        privacy.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", privacy)  # JS fallback

    # click on continue button
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()

    cont_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", cont_btn)
    try:
        cont_btn.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", cont_btn)


def get_popup_text(driver, wait):
    # wait until the alert div exists in the DOM
    el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#alert .alert")))
    # read text using innerText (more reliable than .text for fading toasts)
    return el.get_attribute("innerText").replace("×", "").strip()

#main flow
driver = uc.Chrome()
wait = WebDriverWait(driver, 12)  # single wait object for whole script
try:
    open_homepage(driver, wait)
    go_to_register(driver, wait)

    email = "testone@gmail.com"
    password = "Testone"
    register_user(driver, wait, "Test", "One", email, password)

    msg = get_popup_text(driver, wait)
    print("Popup message:", msg)
    assert "E-Mail Address is already registered" in msg, "Expected 'already registered' warning not shown"
    print("[OK] Negative flow assertion passed")
finally:
    driver.quit()

