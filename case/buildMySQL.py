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
            print("数据库连接错误！",e)

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
        self.cur2.execute('''CREATE TABLE fake1
        user_id INT PRIMARY KEY NOT NULL,
        total_back_amount DECIMAL(10,2) NOT NULL,
        nickname char(255) NOT NULL,
        mail char(255) NOT NULL
        ''')
        print("Table [fake1] created successfully!")

    def insertRecord(self, t_name):
        fake = Faker(locale='zh-CN')
        sql = "INSERT INTO {} (user_id, total_back_amount, nickname, icon) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE total_back_amount = total_back_amount + values(total_back_amount);".format(t_name)
        data = []
        j = 0
        try:
            while j < 500:
                data.append((
                    str(fake.pyint(min_value=0,max_value=9999999,step=1)),
                    fake.pydecimal(right_digits=2,min_value=0,max_value=10000),
                    fake.user_name(),
                    fake.image_url(width=None, height=None)
                ))
                j = j + 1
            self.cur2.executemany(sql, data)
            self.conn2.commit()
            print("500 records inserted!")
        except Exception as e:
            print("插入记录失败！", e)

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
    mysql.insertRecord(t_name=tablename)

    mysql.close()
