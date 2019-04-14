from selenium import webdriver
from time import sleep
import os

class Driver:
    def __init__(self):
        # 初始化和参数配置
        self.driver = webdriver.Chrome()
        self.url = 'https://passport.weibo.cn/signin/login'
        self.account, self.pwd = self.config()
        # 微博登陆
        self.driver.get(self.url)
        sleep(3)
        print(">>>登入账户>>>")
        self.driver.find_element_by_id("loginName").send_keys(self.account)
        print(">>>登入密码>>>")
        self.driver.find_element_by_id("loginPassword").send_keys(self.pwd)
        self.driver.find_element_by_id("loginAction").click()
        print(">>>登录成功>>>")
        sleep(1)

    def config(self):
        os.chdir('../file')
        fhand = open('Config.txt', 'r')
        line = fhand.read().splitlines()
        return line[0], line[1]

    def sign_in(self):
        self.driver.get('https://m.weibo.cn/p/tabbar?containerid=100803_-_followsuper&luicode=10000011&lfid=231093_-_chaohua&page_type=tabbar')
        print('>>>跳转到，我关注的超话>>>')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/div').click()
        print('>>>签到1 - #你是我的命中注定#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div').click()
        print('>>>签到2 - #Jinna#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[4]/div/div/div/div[3]/div').click()
        print('>>>签到3 - #诗词歌芙#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[5]/div/div/div/div[3]/div').click()
        print('>>>签到4 - #傅芙#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[6]/div/div/div/div[3]/div').click()
        print('>>>签到5 - #由你音乐榜#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[7]/div/div/div/div[3]/div').click()
        print('>>>签到6 - #傅英俊#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[8]/div/div/div/div[3]/div').click()
        print('>>>签到7 - #奶酷反差萌傅菁#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[9]/div/div/div/div[3]/div').click()
        print('>>>签到8 - #芙傅何求#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[10]/div/div/div/div[3]/div').click()
        print('>>>签到9 - #傅氏打捞场#')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[11]/div/div/div/div[3]/div').click()
        print('>>>签到10 - #傅菁#')
driver = Driver()
# driver.sign_in()


