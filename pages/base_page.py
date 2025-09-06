# pages/base_page.py
#darkleon1998@gmail.com
#DarkLeon
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=12):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)
        return el

    def get_text(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.get_attribute("textContent").strip()

    # New: wait until the element's text becomes non-empty, then return it
    def get_text_when_non_empty(self, locator):
        def _non_empty_text(d):
            el = d.find_element(*locator)
            txt = (el.get_attribute("textContent") or "").strip()
            return txt if txt else False
        return self.wait.until(_non_empty_text)
