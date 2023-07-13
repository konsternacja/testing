from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://falscify.pl/")
wait = WebDriverWait(driver, 20)

# Click the menu bar
menu_bar = wait.until(EC.element_to_be_clickable((By.ID, 'menu-toggle-icon')))

menu_bar.click()

# Wait until the menu is activated
wait.until(EC.presence_of_element_located(
    (By.XPATH, '//div[contains(@class, "activated")]')))

sign_in_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign up")))

# Click the button
sign_in_btn.click()

wait.until(EC.url_contains('login.html'))
