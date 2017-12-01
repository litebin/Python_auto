from selenium import webdriver
import time
from selenium.webdriver.support.ui  import WebDriverWait

url_1 = 'http://10.214.168.88:7999/aas/v1/auth/loginurl?appId=cpg_website&appSsoUrl=http://10.214.168.88:7999/upp/op/cpg/v1/sso/login?appHomeUrl=http://10.214.168.88:7999/'
account = 'uppadmin'
pwd = '1qazxsw2'

def openBrower():
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle
def openUrl(handle,url):
    handle.get(url)
    handle.maximize_window()
    time.sleep(1)
def findElement(b,arg):
    useEle = b.find_element_by_id(arg['user_id'])
    pwdEle = b.find_element_by_id(arg['pwd_id'])
    loginEle = b.find_element_by_xpath(arg['login_id'])
    return useEle,pwdEle,loginEle
def sendValus(eletuple,arg):
    listkey = ['username_1','pwd_1']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear()                         
        eletuple[i].send_keys(arg[key])
        time.sleep(2)
        i+=1                         
    eletuple[2].click()
def login_test():
    b = openBrower()
    openUrl(b,url_1)
    time.sleep(2)
    ele_dict = {'user_id':'id-input','pwd_id':'password-input',\
                'login_id':'//body//form//button[1]'}
    account_dict = {'username_1':account,'pwd_1':pwd}
    time.sleep(2)
    ele_tuple = findElement(b,ele_dict)
    time.sleep(2)
    sendValus(ele_tuple,account_dict)

if __name__ == '__main__':
     login_test()
