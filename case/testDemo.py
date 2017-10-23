from selenium import webdriver
from time import sleep
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        # 窗口最大化
        self.driver.maximize_window()
        self.msg = '王牌特工2'
        self.url = 'http://www.baidu.com'

    def testSearch(self):
        # open browser
        self.driver.get(self.url)
        sleep(2)
        # click search input
        self.driver.find_element_by_id('kw').click()
        sleep(1)

        # input value
        self.driver.find_element_by_id('kw').send_keys(self.msg)
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(3)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()

