from selenium import webdriver
from selenium.webdriver.common.by import By
import time 




url = "https://the-internet.herokuapp.com/login"

driver = webdriver.Chrome()
driver.get(url)


uname = driver.find_element(By.CSS_SELECTOR,"#username")
password = driver.find_element(By.CSS_SELECTOR,"#password")
login_button = driver.find_element(By.CLASS_NAME, "radius")



uname.send_keys("tomsmith")

password.send_keys("SuperSecretPassword!")

login_button.click()



time.sleep(100)