from selenium import webdriver
import time
from selenium.webdriver.support.ui  import WebDriverWait

url = 'http://www.maiziedu.com/'
login_text = '登录'
account = 'maizi_test@139.com'
pwd = 'abc123456'

def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def login_test():
    b = webdriver.Chrome()
    b.get(url)
    
    b.maximize_window()

    ele_login = get_ele_times(b,10,\
                lambda b: b.find_element_by_link_text('登录'))
    ele_login.click()
    time.sleep(1)
    #b.find_element_by_link_text('登录').click()    
    ac_ele = b.find_element_by_id('id_account_l')
    ac_ele.send_keys(' ')
    ac_ele.clear()
    ac_ele.send_keys(account)
    pwd_ele = b.find_element_by_id('id_password_l')
    time.sleep(1)
    pwd_ele.clear()
    pwd_ele.send_keys(pwd)
    b.find_element_by_id('login_btn').click()
    try:
        #b.find_element_by_link_text('账号或者密码错误，请重新输入')
        b.find_element_by_id('login-form-tips')
        print("Account And Pwd Error!")
    except:
        print("Account And Pwd Right!")
    b.quit()
if __name__ == '__main__':
     login_test()
