from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

usernameInput = driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')
passwordInput = driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
loginButton = driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')

if (usernameInput and passwordInput and loginButton) is not None:
    print('Элементы найдены')
else:
    print('Элементы не найдены')