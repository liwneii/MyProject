
import pymysql

class Mysql():
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost', user='root', password='123456', database='my_db',
                                        charset="utf8")
            self.cursor = self.conn.cursor()  # 游标对象
            print("连接数据库成功")
        except:
            print("连接失败")

    def getItems(self, page, keyword=None):
        sql = "select * from test"
        if keyword:
            sql = sql + " where name like '%" + keyword + "%'"
        start = (int(page) - 1) * 10
        sql = sql + " limit " + str(start) + ",13"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        print(items)
        return items


def main():
    Mysql()

if __name__ == '__main__':
    main()


