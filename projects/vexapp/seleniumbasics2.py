from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.robotevents.com/robot-competitions/vex-robotics-competition')
# element = driver.find_element('name','city')
# element.send_keys('sammamish')
# element = driver.find_element(By.NAME,"city")
# element.send_keys('parth')
# element = driver.find_element(By.ID,"city")
# element.send_keys('parths id')
# element = driver.find_element(By.CLASS_NAME,"form-control")
# element.send_keys('parths fc')

element = driver.find_element(By.CLASS_NAME,"col-sm-6")
print(element.getText())

