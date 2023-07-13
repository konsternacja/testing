# remember about activating corret conda environment

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://falscify.pl/")
wait = WebDriverWait(driver, 20)

# Click the menu bar
menu_bar = wait.until(EC.element_to_be_clickable((By.ID, 'menu-toggle-icon')))

menu_bar.click()

# Wait until the menu is activated
wait.until(EC.presence_of_element_located(
    (By.XPATH, '//div[contains(@class, "activated")]')))

sign_in_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))

# Click the sign in button
sign_in_btn.click()

time.sleep(2)

# Enter email
e_mail = driver.find_element(
    By.XPATH, '//*[@id="email"]').send_keys('Admin@admin.com')

time.sleep(2)

# Enter password
password = driver.find_element(
    By.XPATH, '//*[@id="password"]').send_keys('123')

time.sleep(2)

# Click the sign in button
sign_in_btn = driver.find_element(
    By.XPATH, '/html/body/div/div/div/form/button').click()

time.sleep(2)

error_message = driver.find_element(By.XPATH,
                                    '//div[@class="message-container error-container"]')

# Check if the error message exists
if error_message.is_displayed():
    # Get the text of the error message
    error_text = error_message.text
    print("Error message:", error_text)
else:
    print("Error message not found.")
