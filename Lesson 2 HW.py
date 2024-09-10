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

browser.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
browser.refresh()

#Locators

sleep(15)
browser.find_element(By .XPATH,  "//i[@class='a-icon a-icon-logo']")

sleep(2)

browser.find_element(By. ID, 'ap_email' )
browser.find_element(By.ID, 'continue')
browser.find_element(By .XPATH, "//a[text()='Conditions of Use']")
browser.find_element(By. XPATH, "//a[text()='Privacy Notice']")
browser.find_element(By .XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
browser.find_element(By .XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
browser.find_element(By .XPATH, "//span[@class='a-expander-prompt']")
browser.find_element(By .ID, 'auth-fpp-link-bottom')
browser.find_element(By.ID, 'ap-other-signin-issues-link')
browser.find_element(By.ID, 'createAccountSubmit')

print('Test case passed')
