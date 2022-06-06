from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    troll = browser.find_element(By.XPATH, '//button[@type="submit"]')
    troll.click()


    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    #time.sleep(1)
    browser.switch_to.window(new_window)

    first_window = browser.window_handles[0]

    #button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    #button.click()

    #confirm = browser.switch_to.alert
    #confirm.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()