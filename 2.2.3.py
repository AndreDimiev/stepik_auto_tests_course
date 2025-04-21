import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # Fill text fields
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@example.com")

    # Load file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)

    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("This is a test file.")

    upload_button = browser.find_element(By.ID, "file")
    upload_button.send_keys(file_path)

    # Submit button
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(30)
    browser.quit()
