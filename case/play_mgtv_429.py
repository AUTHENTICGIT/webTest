from selenium import webdriver
from time import sleep

class Driver():
    def __init__(self):
        # 找到firefox插件配置的路径
        self.profile_directory = r'C:\Users\XLY_LR\AppData\Roaming\Mozilla\Firefox\Profiles\glqc2f1m.default'
        # 加载插件配置
        self.profile = webdriver.FirefoxProfile(self.profile_directory)
        # 启动浏览器配置
        self.driver = webdriver.Firefox(self.profile)
        # self.driver = webdriver.Firefox()
        self.url = "https://www.mgtv.com/l/100018346/4351339.html"
        self.loops = 100

    def open(self):
        # 打开页面
        self.driver.get(self.url)
        print('>>> Open Success!--\n'
              '>>> Display loop {1}~1')
        sleep(3)  #等待缓存
        # 2
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[2]').click()
        print('>>> Display loop {1}~2')
        sleep(30)
        # 3
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[3]').click()
        print('>>> Display loop {1}~3')
        sleep(30)
        # 4
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[4]').click()
        print('>>> Display loop {1}~4')
        sleep(30)
        # 5
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[5]').click()
        print('>>> Display loop {1}~5')
        sleep(20)
        print('Loop 1 Complete!')

        for i in range(self.loops):
            # 1
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[1]').click()
            print('>>> Display loop {}~1'.format(i+2))
            sleep(5)
            # 2
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[2]').click()
            print('>>> Display loop {}~2'.format(i+2))
            sleep(5)
            # 3
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[3]').click()
            print('>>> Display loop {}~3'.format(i+2))
            sleep(5)
            # 4
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[4]').click()
            print('>>> Display loop {}~4'.format(i+2))
            sleep(5)
            # 5
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[5]').click()
            print('>>> Display loop {}~5'.format(i+2))
            sleep(5)
            # 1

            print('>>> Loop {} Complete!'.format(i+2))
    def close(self):
        self.driver.close()
driver = Driver()
driver.open()
driver.close()
