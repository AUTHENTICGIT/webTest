from selenium import webdriver
from time import sleep

class Driver:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://passport.weibo.cn/signin/login'
        self.account = 'leogwork@gmail.com'
        self.pwd = 'ksxyhzgdnz007'
    def open(self):
        self.driver.get(self.url)
        sleep(3)
        # 账户
        print(">>>登入账户>>>")
        self.driver.find_element_by_id("loginName").send_keys(self.account)
        sleep(1)
        # 密码
        print(">>>登入密码>>>")
        self.driver.find_element_by_id("loginPassword").send_keys(self.pwd)
        sleep(1)
        # 登录
        self.driver.find_element_by_id("loginAction").click()
        sleep(1)
        print(">>>登录成功>>>")
        sleep(3)
        # zy主页
        self.driver.get("https://m.weibo.cn/status/4169032489925104")
        print(">>>跳转指定微博>>>")
        sleep(5)
        for i in range(50):
            # 转发微博
            print(">>>打开转发框>>>")
            self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/footer/div[1]").click()
            sleep(2)
            print(">>>转发语>>>")
            self.driver.find_element_by_xpath("/html/body/div/div[1]/div/main/div[1]/div/span/textarea[1]").send_keys("[TEST]Auto-Forward Script No." + str(i+1))
            sleep(2)
            # 选择公开/私密
            self.driver.find_element_by_xpath("/html/body/div/div[1]/div/footer/div[1]/div[2]").click()
            sleep(2)
            # 发送
            self.driver.find_element_by_xpath("/html/body/div/div[1]/div/header/div[3]/a").click()
            print(">>>转发第" + str(i+1) +"条>>>")
            sleep(4)
        print("\n脚本结束！共转发" + str(i+1) +"条微博")
    def close(self):
        self.driver.close()

driver = Driver()
driver.open()
