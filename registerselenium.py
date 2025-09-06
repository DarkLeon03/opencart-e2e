
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = uc.Chrome()
driver.get("https://demo.opencart.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 12)  # single wait object for whole script
page_title = driver.title
print(f"The title of the page is: {page_title}")

# Click on My Account -> Register
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()= 'My Account']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class = 'dropdown']//a[text()='Register']"))).click()

# Wait until registration form loads
wait.until(EC.visibility_of_element_located((By.ID,"input-firstname")))

#Enter your personal Details
driver.find_element(By.ID,"input-firstname").send_keys("Test")
driver.find_element(By.ID,"input-lastname").send_keys("One")

# Use an email that is ALREADY REGISTERED
driver.find_element(By.ID,"input-email").send_keys("testone@gmail.com")

#Enter your password
driver.find_element(By.ID,"input-password").send_keys("Testone")

# (Optional) newsletter – if present
try:
    driver.find_element(By.ID,"input-newsletter").click()
except:
    pass

# Agree to Privacy Policy
wait.until(EC.element_to_be_clickable((By.NAME,"agree"))).click()

# click on continue button
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button.btn.btn-primary"))).click()

# Wait for popup alert
try:
    # wait until the alert div exists in the DOM
    el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#alert .alert")))
    # read text using innerText (more reliable than .text for fading toasts)
    msg = el.get_attribute("innerText").replace("×", "").strip()
    print("Popup message:", msg)
except Exception:
    print("Alert not found within timeout")

driver.quit()