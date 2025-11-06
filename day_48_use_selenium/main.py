from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)
# button = driver.find_element(By.ID, value="submit")
# print(button)

events_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(events_time)):
    events[n] = {
        "time": events_time[n].text,
        "name": events_name[n].text
    }

print(events)

driver.quit()