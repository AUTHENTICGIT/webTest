from selenium import webdriver
from time import sleep
import unittest

class Driver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'http://www.baidu.com'
        self.msg = '正义联盟'
    def testSearch(self):
        # open browser
        self.driver.get(self.url)
        sleep(2)
        # input value
        self.driver.find_element_by_id('kw').send_keys(self.msg)
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(1)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()