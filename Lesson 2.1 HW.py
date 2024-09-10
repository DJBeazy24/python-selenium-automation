from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# Start the browser
browser = webdriver.Chrome(service=Service(driver_path))
browser.maximize_window()

browser.get('https://www.target.com/')
sleep(5)

browser.find_element(By .XPATH,"//a[@data-test='@web/AccountLink']").click()
sleep(2)
browser.find_element(By .XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(2)
browser.find_element(By .XPATH, "//span[text()='Sign into your Target account']")

browser.find_element(By.ID, 'login')

print('Test case passed')
browser.quit()
