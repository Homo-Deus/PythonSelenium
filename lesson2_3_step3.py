from selenium import webdriver
import math
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("[type=submit]")
    button.click()
    #browser.switch_to_alert().accept()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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