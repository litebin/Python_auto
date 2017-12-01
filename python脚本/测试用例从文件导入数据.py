from selenium import webdriver
import time
from selenium.webdriver.support.ui  import WebDriverWait
from userdata import get_webinfo
from userdata import get_userinfo


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
    load url
    '''
    handle.get(url)
    handle.maximize_window()

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
        ele_login = get_ele_times(b, 10, lambda b: b.find_element_by_link_text(arg['textid']))
        ele_login.click()
        useEle = b.find_element_by_id(arg['userid'])
        pwdEle = b.find_element_by_id(arg['pwdid'])                              
        loginEle = b.find_element_by_id(arg['loginid'])
        return useEle, pwdEle, loginEle

def sendVals(eletuple,arg):
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
        i+=1
    time.sleep(2)
    eletuple[2].click()
    
def checkResult(b,errorid):
    try:
        err = b.find_element_by_id(errorid)
        print('Account And Pwd Error!')
        print(err.text)
    except:
        print('Account And Pwd Right!')
                                  
def login_test(ele_dict,account_dict):
    b = openBrower()
    openUrl(b, ele_dict['url'])                              
    time.sleep(2)
    ele_tuple = findElement(b,ele_dict)
    time.sleep(2)
    #for arg in account_dict:
    sendVals(ele_tuple, account_dict)
    checkResult(b,ele_dict['errorid'])
                                  
    

   
if __name__ == '__main__':
    url = 'http://www.maiziedu.com/'
    login_text = '登录'
    account = 'maizi_test@139.com'
    pwd = 'abc123456'
    '''
    ele_dict = {'url':url,'textid':login_text, 'userid':'id_account_l',\
                'pwdid':'id_password_l', 'loginid':'login_btn','uname':account,\
                'pwd':pwd,'loginError':'//body//div//form/following-sibling::div[1]/div[1]',\
                'errorid':'该账号格式不正确'}
    account_dict = [{'uname':account, 'pwd':pwd}]
    '''
    ele_dict = get_webinfo(r'C:\Users\Administrator\Desktop\python脚本\webinfo.txt')
    
    account_dict = get_userinfo(r'C:\Users\Administrator\Desktop\python脚本\userinfo.txt')
    #file webinfo/userinfo ele_dict = get_webinfo(path) account_dict = get_userinfo(path)
    login_test(ele_dict,account_dict)
