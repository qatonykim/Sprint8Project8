from selenium import webdriver

driver = webdriver.Chrome() # create Chrome driver
driver.maximize_window() # Full screen mode

driver.get('https://google.com/')  #navigate to the url
current_url = driver.current_url   # get current url
assert 'google.com' in driver.current_url # verify if google.com in the current url
driver.quit()