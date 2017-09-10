import os
from selenium import webdriver

# create new Edge session
dir = os.path.dirname(__file__)
edge_path = dir + "\MicrosoftWebDriver.exe"
driver = webdriver.Edge("\edge_server\MicrosoftWebDriver.exe")
driver.implicitly_wait(10)
# driver.maximize_window()

driver.get("https://www.google.com/")

# get the search textbox
search_field = driver.find_element_by_name("q")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
lists = driver.find_elements_by_class_name("r")

# get the number of elements found
print("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i = 0
for listitem in lists:
    print(listitem)
    i = i + 1
    if (i > 10):
        break

# close the browser window
driver.quit()