import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/find_link_text"
    browser.get(link)

    # Calculate the text for the link
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    # Find the link by its text
    element_link = browser.find_element(By.LINK_TEXT, link_text)
    element_link.click()

    # Find the form elements and fill them out
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Click the submit button
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Wait for the page to load and get the confirmation code
    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(30)
    browser.quit()
