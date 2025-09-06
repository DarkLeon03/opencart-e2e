# D:\opencart-e2e\tests\conftest.py
import pytest
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    opts = uc.ChromeOptions()
    # disable password manager + save bubble
    opts.add_experimental_option("prefs", { "credentials_enable_service": False, "profile.password_manager_enabled": False,})
    opts.add_argument("--disable-save-password-bubble")
    opts.add_argument("--no-first-run")
    opts.add_argument("--no-default-browser-check")

    drv = uc.Chrome(options=opts)
    drv.maximize_window()
    yield drv
    drv.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 12)
