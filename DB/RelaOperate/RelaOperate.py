from pymysql import *

def dataPrint():

    # connection
    conn = connect(host='127.0.0.1', port=3306, user='root', password='123456', database='my_db', charset='utf8')
    # get Cursor object
    cs1 = conn.cursor()


    cs1.execute('select * from test;')
    line_content = cs1.fetchmany(size=3)
    print(line_content)
    print(line_content[0], line_content[1])
    for tmp in line_content:
        print(tmp)
        for tmp_1 in tmp:
            print(tmp_1)
    cs1.close()
    conn.close()

if __name__ == '__main__':
    dataPrint()


 #
    # cs1.execute('select * from test;')
    # line_content = cs1.fetchone()
    # print(line_content)
    # print(line_content[0], line_content[1])
    # for tmp in line_content:
    # # (1, 'swk', 18, 'male', 0, None, b'\x00')
    # # 1
    # # swk
    # # 1
    # # swk
    # # 18
    # # male
    # # 0
    # # None
    # # b'\x00'


    # execute select, return rows of selected
    # count = cs1.execute('select id,name from student where id > 1')
    # print("the numbers of rows is %d" % count)
    # data = cs1.fetchone()
    # print(data)
    # data1 = cs1.fetchmany(2)
    # print(data1)
    # data2 = cs1.fetchall()
    # print(data2)
    # # the numbers of rows is 3
    # # (2, 'zbj')
    # # ((3, 'zbj'), (4, 'shs'))
    # # ()

