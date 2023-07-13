# remember about activating corret conda environment

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://falscify.pl/")
wait = WebDriverWait(driver, 10)

# Wait for the button to be clickable
button = wait.until(
    EC.element_to_be_clickable((By.ID, 'theme-toggle-btn')))

# Click the button
button.click()

# Wait until the body element has the specified class
wait.until(EC.presence_of_element_located(
    (By.XPATH, '//body[contains(@class, "light theme")]')))
