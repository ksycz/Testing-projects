#importing needed modules
import unittest
from selenium import webdriver
#import keys on the keyboard
from selenium.webdriver.common.keys import Keys
#test case
class TestMyStoreHomePage(unittest.TestCase):
#set up method
    def setUp(self):
        self.driver = webdriver.Firefox()
#testing search
    def test_search_in_my_store(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        self.assertIn("My Store", driver.title)
        elem = driver.find_element_by_name("search_query")
        #return search results
        elem.send_keys("summer dress")
        elem.send_keys(Keys.RETURN)
        assert "No results found" not in driver.page_source
  #  def tearDown(self):
      #  self.driver.quit()

if __name__ == "__main__":
    unittest.main()
