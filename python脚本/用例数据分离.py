from selenium import webdriver
import time
from selenium.webdriver.support.ui  import WebDriverWait



def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def openBrower():
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle

def openUrl(handl,url):
    handle.get(url)
    handle.maximize_window()

def findElement(b,arg):
        ele_login = get_ele_times(b,10,lambda b b.find_element_by_link_text(arg['text_id']))
        ele_login.click()
        useEle = b.find_element_by_id(arg['userid'])
        pwdEle = b.find_element_by_id(arg['pwdid'])
        loginEle = b.find_element_by_id(arg['loginid'])
        return useEle,pwdEle,loginEle
def sendVals(eletuple,arg):
    listkey = ['uname','pwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear()                         
        eletuple[i].send_keys(arg[key])
        i+=1
    time.sleep(2)
    eletuple[2].click()
