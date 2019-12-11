from selenium import webdriver
import math
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element_by_css_selector("input[placeholder~=first]")
    firstName.send_keys("Ivan")

    lastName = browser.find_element_by_css_selector("input[placeholder~=last]")
    lastName.send_keys("Petrov")

    email = browser.find_element_by_css_selector("input[placeholder~=email]")
    email.send_keys("email.email.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'pythonTest.txt')

    attach = browser.find_element_by_id("file")
    attach.send_keys(file_path)

    submit = browser.find_element_by_xpath("//button[text()='Submit']")
    submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()