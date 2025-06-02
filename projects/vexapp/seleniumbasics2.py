from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.robotevents.com/robot-competitions/vex-robotics-competition')
element = driver.find_element('name','city')
element.send_keys('sammamish')
