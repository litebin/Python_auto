from selenium import webdriver
import time
from selenium.webdriver.support.ui  import WebDriverWait

url = 'http://www.maiziedu.com/'
login_text = '登录'
account = 'maizi_test@139.com'
pwd = 'abc123456'

def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def openBrower():
    '''
    return webdriver Handle
    '''
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle

def openUrl(handle,url):
    '''
    lod url
    '''
    handle.get(url)
    handle.maximize_window()
time.sleep(1)

def findElement(b,arg):    
    '''
    arg must be dict
    1:text_id:
    2:userid
    3:pwdid
    4:loginid
    return useEle, pwdEle, loginEle
    '''
    for text_id in arg:
        ele_login = get_ele_times(b,10, lambda b: b.find_element_by_link_text(arg['text_id']))                                 
        ele_login.click()
        useEle = b.find_element_by_id(arg['userid'])
        pwdEle = b.find_element_by_id(arg['pwdid'])                              
        loginEle = b.find_element_by_id(arg['loginid'])
        return useEle, pwdEle, loginEle

def sendVals(eletuple, arg):
    '''
    ele tuple
    account : uname , pwd
    '''
    listkey = ['uname','pwd']
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
   
    openUrl(b,url)
    time.sleep(2)
                                  #定义一个元组
    ele_dict = {'text_id':login_text, 'userid':'id_account_l',\
                'pwdid':'id_password_l', 'loginid':'login_btn'}
    account_dict = {'uname':account, 'pwd':pwd}
    time.sleep(2)
    ele_tuple = findElement(b,ele_dict)
    time.sleep(2)
    sendVals(ele_tuple, account_dict)
                                  
    

   
if __name__ == '__main__':
     login_test()
