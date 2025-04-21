import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/get_attribute.html")

    chest_image = driver.find_element(By.ID, "treasure")
    x = chest_image.get_attribute("valuex")
    y = calc(x)

    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule_radio = driver.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(30)
    driver.quit()
