from selenium import webdriver
from selenium.webdriver.common.by import By

try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.ID, "button")
    
    


finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()