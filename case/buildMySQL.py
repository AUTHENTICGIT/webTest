from faker import Faker
import pymysql

class Mysql():
    def __init__(self, dbname):
        self.dbname = dbname
        try:
            self.conn1 = pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='information_schema')
            self.conn2 = pymysql.connect(host='localhost',port=3306, user='root', passwd='', db=self.dbname)
            print(self.conn1)
            print(self.conn2)
            print('Connect database [{}] successfully!'.format(self.dbname))
            self.cur1 = self.conn1.cursor()
            self.cur2 = self.conn2.cursor()
        except Exception as e:
            print(e)

    def checkExist(self, t_name):
        sql = "SELECT table_name FROM tables WHERE table_schema = '{}' AND table_type LIKE '%table%' AND table_name = '{}'".format(self.dbname,t_name)
        self.cur1.execute(sql)
        print(sql)

        if self.cur1.fetchone():
            print("存在这张表！")
            return 1
        else:
            print("表不存在！")
            return 0

    def createTable(self):
        pass

    def insertRecord(self):
        pass

    def close(self):
        self.conn2.close()
        self.conn1.close()

if __name__ == '__main__':
    dbname = input("Connect Your Database:")
    mysql = Mysql(dbname)
    tablename = input("Enter Your Table Name:")
    ret = mysql.checkExist(t_name=tablename)
    if ret == 0:
        enter = input("Do you wanna build one? (Yes/No)")
        if enter == 'Yes':
            mysql.createTable()
            print("built!")

    mysql.close()
