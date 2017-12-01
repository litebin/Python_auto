from selenium import webdriver 
import time
 
browser = webdriver.Chrome(r'D:\python\chromedriver.exe') 
browser.get('http://www.baidu.com') 
 
browser.maximize_window()
 
browser.find_element_by_id('kw').send_keys('selenium')  
 
browser.find_element_by_id('su').click()
 
time.sleep(3)
 
browser.quit()
