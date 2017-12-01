class OpenChrome(unittest.TestCase):
    def setUp(self):
       
        self.chromedriver = "D:\\pythonn\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = self.chromedriver
       
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver= webdriver.Chrome(self.chromedriver,chrome_options=options)
       
        self.driver.maximize_window()
        
        
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_open_chrome(self):
        driver = self.driver
        driver.get(self.base_url)
        try: self.assertEqual("百度一下，你就知道", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
