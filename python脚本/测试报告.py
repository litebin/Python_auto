from selenium import webdriver  
import unittest,time  
import HTMLTestRunner
classMyTest():
     def setUp(self): 
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()  
        self.driver.implicitly_wait(10)  
        self.base_url ="http://www.baidu.com"  
         
    def test_baidu(self):
        driver = self.driver  
        driver.get(self.base_url +"/")  
        driver.find_element_by_id("kw").clear()  
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")  
        driver.find_element_by_id("su").click()  
    def tearDown(self):  
        self.driver.quit()  
if__name__=="__main__":
    testSuite=unittest.TestSuite()  
    testSuite.addTest(MyTest("test_baidu"))  
    Html=".\\result.htm"  
    fp=file(Html,'wb')  
   
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况：')  
    runner.run(testSuite)  
    fp.close()  
