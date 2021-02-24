from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_css_selector("#book").click()
    
    browser.find_element_by_css_selector("#answer").send_keys(calc(browser.find_element_by_css_selector("#input_value").text))
    browser.find_element_by_css_selector("#solve").click()
    
finally:
    time.sleep(10)
    browser.quit()