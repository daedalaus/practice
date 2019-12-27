from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input_el = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# input_el.send_keys("女包")
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# button.click()
print(input_el, button)
