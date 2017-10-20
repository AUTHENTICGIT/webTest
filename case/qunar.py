from selenium import webdriver
from time import sleep
import unittest

class Driver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = 'https://flight.qunar.com'
        self.fromCity = '成都'
        self.toCity = '上海'
    def testSearch(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.find_element_by_name('fromCity').click()
        sleep(1)
        self.driver.find_element_by_name('fromCity').send_keys(self.fromCity)
        sleep(1)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()