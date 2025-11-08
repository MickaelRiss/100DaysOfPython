import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ACCOUNT_EMAIL = "mickael@test.com"
ACCOUNT_PASSWORD = "03849@mickael"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

# Automated Login
login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email = driver.find_element(By.ID, "email-input")
password = driver.find_element(By.ID, "password-input")
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)

wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# Find first Thursday
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    print(card.text)
    print("Parent element:")
    print(card.parent)
    print("=========\n")

driver.quit()