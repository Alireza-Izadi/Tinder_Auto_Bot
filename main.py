import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

FACEBOOK_EMAIL = "ENTER YOUR FACEBOOK LOGIN EMAIL"
FACEBOOK_PASSWORD = "ENTER YOUR FACEBOOK PASSWORD"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("tinder.com")

# Finding Login Button And Click On It
time.sleep(5)
login_button = driver.find_element(
    By.XPATH,
    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button',
)
login_button.click()
# Finding Facebook Login Section And Click On It
time.sleep(5)
fb_login = driver.find_element(
    By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button'
)
fb_login.click()
# Windows Pop Up Management
time.sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
# Finding Email And Password Input
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
# Sending Our Email And Password Login Credentials
email.send_keys(FACEBOOK_EMAIL)
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)
# After Facebook Login Pop Up Switching back to the main window
driver.switch_to.window(base_window)
print(driver.title)
# Allowing Access To Location
time.sleep(5)
allow_location_button = driver.find_element(
    By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
)
allow_location_button.click()
notifications_button = driver.find_element(
    By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]'
)
# Allow Cookies
notifications_button.click()
cookies = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button'
)
cookies.click()
# ------------------------------The Swiping Function -----------------------#
# It Is Up To 100 Times Change it if you want
for n in range(100):
    time.sleep(3)
    try:
        print("called")
        like_button = driver.find_element(
            By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button',
        )
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(6)

driver.quit()
# ========================================A.I================================================ #
