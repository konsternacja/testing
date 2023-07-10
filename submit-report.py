from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://falscify.pl/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# Wait for the button to be clickable
submit_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/div/div/div[2]/a/button')))

# Click the button
submit_btn.click()
time.sleep(5)

# Wait until the body element has the specified class
wait.until(EC.url_contains('login.php'))
