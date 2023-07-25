
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 
    def test_a_success_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

    # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Products', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()