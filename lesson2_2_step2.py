from selenium import webdriver
import math
import time

from selenium.webdriver.support.select import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_atrb = browser.find_element_by_id("num1").text
    second_atrb = browser.find_element_by_id("num2").text
    sum = int(first_atrb) + int(second_atrb)

    dropDownValue = Select(browser.find_element_by_class_name("custom-select"))
    dropDownValue.select_by_value(str(sum))

    submit = browser.find_element_by_xpath("//button[text()='Submit']")
    submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()