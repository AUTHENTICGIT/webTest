from selenium import webdriver
from time import sleep
import unittest
import datetime

class Driver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        self.url = 'https://flight.qunar.com'
        self.fromCity = '成都'
        self.toCity = '上海'
        self.date = str(datetime.date.today() + datetime.timedelta(days=7))
    def testSearch(self):
        self.driver.get(self.url)
        sleep(3)
        # 选择出发城市：成都
        self.driver.find_element_by_name('fromCity').click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div/div[3]/div[1]/form/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/dl/dd/ul/li[3]/a").click()
        sleep(1)
        # 选择到达城市：上海
        self.driver.find_element_by_name('toCity').click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div/div[3]/div[1]/form/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/a").click()
        sleep(1)
        # 选择today+7日后的日期
        self.driver.find_element_by_name('fromDate').clear()
        self.driver.find_element_by_name('fromDate').send_keys(self.date)
        # 搜索
        self.driver.find_element_by_class_name('btn_search').click()
        sleep(10)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()