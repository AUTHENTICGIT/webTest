import requests

def getHomePage():
    uid = '5330680265'
    url = 'https://weibo.com/u/' + uid + '?profile_ftype=1&is_all=1#_0'
    return url

def getFromData(pro_id, num):
    FromData = {
        'pro_id':pro_id,
        'type':1,
        'page':1,
        'pageSize':num
    }
    return FromData

def getBlogList():
    # 模拟post请求，从mbloglist获得返回到json数据
    FromData = getFromData(id, num)
    r = requests.post('')

def insert():
    pass

def main():
    pass