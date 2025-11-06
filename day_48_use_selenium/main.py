from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.CLASS_NAME, value="top")
last_name = driver.find_element(By.CLASS_NAME, value="middle")
email = driver.find_element(By.CLASS_NAME, value="bottom")

first_name.send_keys("Mickael")
last_name.send_keys("Riss")
email.send_keys("mickael.riss@yahoo.fr", Keys.ENTER)

# search_input = driver.find_element(By.NAME, value="search")
# search_input.send_keys("Python", Keys.ENTER)

driver.quit()