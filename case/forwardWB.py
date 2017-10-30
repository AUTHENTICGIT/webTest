from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://weibo.com/'
        self.account = 'leogwork@gmail.com'
        self.pwd = 'ksxyhzgdnz007'
    def open(self):
        self.driver.get(self.url)
        sleep(20)
        # 账户
        self.driver.find_element_by_id('loginname')
        sleep(1)
        print(">>>登入账户>>>")
        sleep(1)
        self.driver.find_element_by_id('loginname').send_keys(self.account)
        sleep(1)
        # 密码
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[2]/div/input")
        sleep(1)
        print(">>>登入密码>>>")
        sleep(1)
        self.driver.find_element_by_css_selector(".password > div:nth-child(1) > input:nth-child(1)").send_keys(self.pwd)
        sleep(1)
        # 登录
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[6]/a").click()
        sleep(1)
        print(">>>登录成功>>>")
        sleep(10)
        # 个人主页
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/div/a/img").click()
        # zy主页
        self.driver.get("http://weibo.com/u/3668829440")
        print(">>>定位转发主页>>>")
        sleep(3)
        for i in range(10):
            # 转发微博
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[3]/div/div[3]/div[2]/div/ul/li[2]/a/span/span").click()
            print(">>>打开转发框>>>")
            sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/textarea").click()
            print(">>>转发语>>>")
            sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/textarea").send_keys("[TEST]Auto-Forward Script No." + str(i+1))
            sleep(3)
            # 选择公开/私密
            self.driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/a/i").click()
            print(">>>选择公开/私密>>>")
            sleep(3)
            # 好友圈可见
            self.driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div/ul/li[2]/a").click()
            print(">>>好友圈可见>>>")
            sleep(3)
            # 好友发布
            self.driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/a").click()
            print(">>>转发第" + str(i+1) +"条>>>")
            sleep(3)
        print("\n脚本结束！共转发" + str(i+1) +"条微博")
    def close(self):
        self.driver.close()
driver = Driver()
driver.open()
