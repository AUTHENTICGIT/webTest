from selenium import webdriver

class Driver:
    def __init__(self, url):
        self.browser = webdriver.Chrome()
        self.url = url
    def open_browser(self):
        """
        Do something for browser
        :return: browser
        """
        # 窗口最大化
        self.browser.maximize_window()

        # 打开地址链接
        self.browser.get(self.url)
        return self.browser
    def close_browser(self):
        """
        quit browser
        :return:
        """
        self.browser.quit()

url = input('Enter the website:')
d = Driver(url)
d.open_browser()