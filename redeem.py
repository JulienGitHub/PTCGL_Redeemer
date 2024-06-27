from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time

#Your Pokémon credentials
_username = "USERNAME"
_password = "PASSWORD"

#init selenium
driver = Driver(uc=True)

#load redeem page
driver.get('https://redeem.tcg.pokemon.com/')

#wait 2 seconds (redirection to the login page)
time.sleep(5)

#find email and password fields, fill them with your data
userID = driver.find_element(By.ID, "email")
userID.click()
time.sleep(2)
userID.send_keys(_username)
#wait 2 seconds (redirection to the login page)
time.sleep(2)
password = driver.find_element(By.ID, "password")
password.click()
time.sleep(2)

password.send_keys(_password)
time.sleep(2)
#find Log In button and click on it
login_button = driver.find_element(By.CSS_SELECTOR, "[id='accept']")
login_button.click()

#wait 2 seconds (redirection to the actual redeem page)
time.sleep(4)

cookies_button = driver.find_element(By.CSS_SELECTOR, "[id='onetrust-reject-all-handler']")
cookies_button.click()
time.sleep(1)

#open codes.txt and store the codes
f = open("codes.txt", "r")
codes = f.readlines()
f.close()

codesCounter = 0
#for all the codes
for code in codes:
	code = code.replace('\n', '')
	print(code)
	#find the code field and fill it
	codeField = driver.find_element(By.ID, "code")
	codeField.send_keys(code)
	#find the verify button and click it
	submitCode_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='verify-code-button']")
	submitCode_button.click()
	time.sleep(3)
	codesCounter += 1
	if(codesCounter == 10):
		#if 10 codes
		codesCounter = 0
		#find the redeem button and click it
		submitCode_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='button-redeem']")
		submitCode_button.click()
		time.sleep(5)
submitCode_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='button-redeem']")
submitCode_button.click()
time.sleep(5)
driver.quit()
