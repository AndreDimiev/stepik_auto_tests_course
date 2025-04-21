import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # Click the button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Accept the confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # Solve the captcha on the new page
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(30)
    browser.quit()
