from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID,"num1")
    y_element = browser.find_element(By.ID,"num2")
    x = int(x_element.text)
    y = int(y_element.text)
    z = str(x + y)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z) 
    button = browser.find_element(By.XPATH,'//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()