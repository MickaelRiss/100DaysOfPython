from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar)
button = driver.find_element(By.ID, value="submit")
print(button)

driver.quit()