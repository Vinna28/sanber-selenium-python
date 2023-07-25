
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class LoginTesting(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
 
    def test_a_success_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("ropa01@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("Testing4321") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[normalize-space()='login'])[1]").click()
        time.sleep(1)

    # validasi
        response_data = driver.find_element(By.CLASS_NAME,"css-1mqa38q").text
        self.assertIn('dashboard', response_data)

    def test_a_failed_login_with_wrong_password(self): 
    # steps
        driver = self.browser #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("ropa01@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("Testing321") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[normalize-space()='login'])[1]").click()
        time.sleep(1)

    # validasi
        response_data = driver.find_element(By.XPATH,"(//div[@role='alert'])[1]").text
        self.assertIn("Kredensial yang Anda berikan salah", response_data)


    def test_a_failed_login_with_empty_email_and_password(self): 
    # steps
        driver = self.browser #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[normalize-space()='login'])[1]").click()
        time.sleep(1)

    # validasi
        response_data = driver.find_element(By.XPATH,"(//div[@role='alert'])[1]").text
        self.assertIn('"email" is not allowed to be empty', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()