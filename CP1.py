import HtmlTestRunner
import time 
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()
        time.sleep(2)  # Espera de 2 segundos

    def test_login1(self):
        self.user=self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
        self.password=self.driver.find_element(By.XPATH,"//input[contains(@type,'password')]").send_keys("admin123")
        self.button=self.driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Login')]")
        self.button.click()
        time.sleep(7)  # Espera de 5 segundos

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Prueba exitosa. El navegador se ha cerrado correctamente.")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))