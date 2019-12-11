import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100')
    )

    book = browser.find_element_by_xpath("//button[text()='Book']")
    book.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element_by_css_selector("#answer")
    input_field.send_keys(y)

    submit = browser.find_element_by_xpath("//button[text()='Submit']")
    submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()