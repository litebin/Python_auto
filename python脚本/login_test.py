from selenium import webdriver
import time

url = 'http://www.maiziedu.com/'
login_text = '登录'
account = 'maizi_test@139.com'
pwd = 'abc1234567'

def login_test():
    b = webdriver.Chrome()
    b.get(url)
    time.sleep(3)
    b.maximize_window()
    time.sleep(1)
    b.find_element_by_link_text('登录').click()
    time.sleep(1)
    ac_ele = b.find_element_by_id('id_account_l')
    time.sleep(1)
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

if __name__ == '__main__':
     login_test()
