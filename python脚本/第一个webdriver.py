import selenium
from selenium import webdriver
import time

broswer = webdriver.Chrome()
broswer.get("http://10.214.168.88:8080/aas/v1/auth/loginurl?appId=cpg_website&appSsoUrl=http://10.214.168.88:8080/upp/op/cpg/v1/sso/login?appHomeUrl=http://10.214.168.88:8080/")
broswer.maximize_window()
assert "万达网络科技客服系统" in broswer.title

acc_ele = broswer.find_element_by_xpath("//div//form/input[4]")
acc_ele.clear()
acc_ele.send_keys("uppadmin")
pwd_ele = broswer.find_element_by_xpath("//div//form/input[5]")
pwd_ele.clear()
pwd_ele.send_keys("1qazxsw2")
dl_ele = broswer.find_element_by_css_selector("html body div.container div.login-box form#loginForm button.submit-button")
dl_ele.click()
time.sleep(3)
broswer.find_element_by_xpath("//body//ul//li[3]//li[1]/a[1]").click()

