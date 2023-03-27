import requests
import re
from lxml import html
import pymysql


class reptile():
    # def func(self):
    #     # url = 'https://movie.douban.com/'  # 需要爬数据的网址
    #     url = 'https://movie.douban.com/top250?start=0&filter='
    #     page = requests.Session().get(url)
    #     tree = html.fromstring(page.text)
    #     result = tree.xpath('//li[@class="title"]//a/text()')  # 获取需要的数据
    #
    # def func1(self):
    #     r = requests.get("http://read.douban.com/provider/all")
    #     htmltext = r.text
    #     # print(htmltext)
    #     html = re.findall(r'<a href="/provider/63687123/"(.*?)</section>', htmltext, re.S)[0]
    #     htmlchubanshe = re.findall(r'<div class="name"(.*?)</div>', html, re.S)
    #     fh = open("E:\\Pythondemo\\Python-test\\PythonLX\\chubanshe.txt", "w")
    #     for cbs in htmlchubanshe:
    #         print(cbs)
    #         fh.write(cbs + "\n")
    #     fh.close()
    #
    # def func2(self):
    #     response = requests.get("http://www.baidu.com")  # 生成一个response对象
    #     response.encoding = response.apparent_encoding  # 设置编码格式
    #     print("状态码:" + str(response.status_code))  # 打印状态码
    #     print(response.text)  # 输出爬取的信息

    def func3(self):
        response = requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")  #get方法的到图片响应
        file = open("D:\\mydata\\MyProject\\Reptile\\baidu_logo.gif","wb") #打开一个文件,wb表示以二进制格式打开一个文件只用于写入
        file.write(response.content) #写入文件
        file.close()#关闭操作，运行完毕后去你的目录看一眼有没有保存成功

def main():
    reptile().func3()

if __name__ == '__main__':
    main()