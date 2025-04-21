import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    time.sleep(10)

finally:
    time.sleep(30)
    browser.quit()
