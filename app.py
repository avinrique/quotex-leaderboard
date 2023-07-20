from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
chrome_driver_path = '/usr/local/bin/chromedriver'
service = webdriver.chrome.service.Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://qxbroker.com/en/sign-up/fast/')
sleep(2)
button = driver.find_element(By.XPATH, '//button[@data-text="Top"]')
button.click()
sleep(2)
element = driver.find_element(By.CLASS_NAME, 'panel-leader-board__items')
driver.implicitly_wait(5)
print(element.text)
#panel-leader-board__items
driver.quit()
