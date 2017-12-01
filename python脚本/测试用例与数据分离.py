from selenium import webdriver
import time
from selenium.webdriver.support.ui  import WebDriverWait


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

def checkResult(b,ele_dict):
    eerorEle = b.find_element_by_id(arg['login-form-tips'])
    return eerorEle
    
                                  
def login_test(ele_dict,user_dict):
    b = openBrower()
    openUrl(b,ele_dict['url'])
    
                                  #定义一个元组    
    time.sleep(2)
    ele_tuple = findElement(b,ele_dict)
    time.sleep(2)
    for arg in user_dict:        
        sendVals(ele_tuple, arg)
        checkResult(b,ele_dict['errorid'])                        
    

   
if __name__ == '__main__':
    url = 'http://www.maiziedu.com/'
    login_text = '登录'
    account = 'maizi_test@139.com'
    pwd = 'abc123456'
    ele_dict = {'url':url,'text_id':login_text, 'userid':'id_account_l',\
                'pwdid':'id_password_l', 'loginid':'login_btn','uname':account, 'pwd':pwd,\
                'errorid':'login-form-tips'}
    user_dict = [{'uname':account, 'pwd':pwd}]
    login_test(ele_dict,user_dict)
