from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn = browser.find_element(By.XPATH, '//button[@id="book"]')
    btn.click()

    #browser.execute_script("window.scrollBy(0, 100);")
    #button = browser.find_element(By.ID, "book")
    #button.click()


    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[@id="solve"]')
    button.click()

finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()