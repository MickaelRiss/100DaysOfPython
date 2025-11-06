from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load
sleep(2)

# By pass language
try:
    fr_language = driver.find_element(By.ID, value="langSelect-FR")
    fr_language.click()
except NoSuchElementException:
    print("Language not find.")

# Wait for page to load
sleep(2)

cookie = driver.find_element(By.ID, value="bigCookie")

# Check purchase every 5sec
timeout = time() + 5
five_min = time() + 60 * 5
click = True

while click:
    cookie.click()

    if time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, value="#products .product")
        for item in reversed(items):
            if item.get_attribute("class") == "product unlocked enabled":
                item.click()

    if time() > five_min:
        click = False

driver.quit()