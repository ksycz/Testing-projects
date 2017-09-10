#importing needed modules
import unittest
import time
from selenium import webdriver
#import keys on the keyboard
from selenium.webdriver.support.ui import WebDriverWait
#test case
class SignInTest(unittest.TestCase):
#set up method
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        self.driver.maximize_window()
#testing sign in
    def test_sign_in_my_store(self):
        #testing data
        driver = self.driver
        mystoreUsername = 'ks_test@domain.com'
        mystorePassword = 'KSTest'

        emailFieldID = 'email'
        passFieldID = 'passwd'
        loginButtonXpath = '//*[@id="SubmitLogin"]'
        orderHistoryPath = '//*[@id="center_column"]/div/div[1]/ul/li[1]/a/span'

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(mystoreUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(mystorePassword)
        loginButtonElement.click()
        #checking if we are signed in = checking if the Order history and details button appears
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(orderHistoryPath))

        #  def tearDown(self):
        #  self.driver.quit()

if __name__ == "__main__":
    unittest.main()