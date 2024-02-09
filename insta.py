from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from password import username1, password1
import time

def log_in(username, password):
    # Set up the Chrome driver
    driver = webdriver.Chrome()

    driver.get("https://www.instagram.com/accounts/login/")

    time.sleep(2)

    try:
        # Find the username and password fields
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

        # Enter your username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Press Enter to submit the login form
        password_field.submit()

        # Wait for the login process to complete
        WebDriverWait(driver, 10).until(EC.title_contains("Instagram"))
    
        try:
            profile_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft']")))
            profile_icon.click()
            print("Clicked on the profile icon")
        except TimeoutException:
            print("Profile icon not found within the specified time")

    except NoSuchElementException as e:
        print(f"Error: {e}")

    except TimeoutException as e:
        print(f"Timeout error: {e}")

log_in(username1,password1)