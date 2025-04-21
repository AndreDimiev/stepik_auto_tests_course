import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Wait until the price drops to $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Click the "Book" button
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Solve the math problem on the new page
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(30)
    browser.quit()
