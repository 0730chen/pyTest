# from socket import socket
# def main():
#     client = socket()
#     client.connect(('127.0.0.1',3000))
#     print(client.recv(1024).decode('utf-8'))
#     client.close()

# if __name__ == '__main__':
#     main()
import requests
from bs4 import BeautifulSoup

# r = requests.get('https://www.baidu.com/')
# print(r.text)
# 1.选取要爬取得网站url
# 2.爬取内容
# 3.将爬到的内容存在文件中
def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url,headers = headers)
    return r.text
def get_content(html):
    soup = BeautifulSoup(html,'lxml')
    reviewList = soup.find_all('div',{'class':'review-list'})#要将可遍历字符串对象转变成标签对象，然后获取其中的属性值
    # print(type(movielist))
    # print(movielist)
    # print(reviewList)
    # titles = "作者：{} 标题: {} 评论{}\n------------\n" # 最终输出格式
    
    for review in reviewList:
        #查找到点评电影名称
        
        movieTitle = review.find_all('img',title = True)#使用定向索引只提取title属性标签
        #查找作者id
        actId = review.find_all('a',{'class':'name'})
        # titleS = movieTitle.find('img')
        # print(movieTitle)
        # print(actId)
        contents = review.find_all('div',{'class':'short-content'})
        # print(review)
        # print(contents)
       
       
        date = []
        for title in movieTitle:
            # print(title['title'])
            # titles.append(title['title'])
            Dtitle = title['title']
            date.append(Dtitle)
            
            # titles.append(Dtitle)
        for actid in actId:
            # titles.append(actid.string)
            Dactid = actid.string
            # titles.append(Dactid)
            # print(actid.string)
            date.append(Dactid)
            
            
        for content in contents :
            # print(content.get_text()) 
            Dcontent = content.get_text()
            # titles.append(Dcontent)
            
            date.append(Dcontent)
        return date   
    
    # print(titles)
    # save(titles.format(Dactid,Dtitle,Dcontent))
            
    
    
    
        

        #     # print(type(title))
        #     # print(type(title))
        #     print(title)
            # print(title['alt'])
        # print(movieTitle)
        # print(review)

        # title = movie['data-title']
        # print(title)
        # title = movie.find(class_='list-item')
        # print(title)
        # title = movie.find('img')
        # print(title)
        # print(type(movie))
        # print(movie)
    #    socre = movie.find('span')
    #    print(socre)
        # # print(type(movie)
       
        
    #     # # # title = movie.find('data-title')
    #     # print(title)

    # print(movie)
def save(lists):
    # for i in args:不返回一个list，直接输出，然后保存。args是获取到的数值
    #     with open('./douban.text','w+',encoding="utf-8") as f:
    #         f.write('hello world')
    #         f.write(i)
            # print(i+'我是写入文件的i')
            # print(f.readlines())
    with open('./douban.text','a+' ,encoding ="utf-8") as f:
        for content in lists:
            f.write(content)
        print('当前页面保存完成')
    
        
def main():
    
    urlList = []
    for i in range(0,5):
        url = 'https://movie.douban.com/review/best/?start={}'.format(i*10)
        urlList.append(url)
        # print(urlList)
    
    for url in urlList:
        html = download_page(url)
        content = get_content(html)
        save(content)
        
        # save(contents)
        print(content)
    print('保存全部信息')
    
    


        # html = download_page(url)
        # get_content(html,i*10)
        # print(url)
    # url = 'https://movie.douban.com/review/best/?start=0'
    # html = download_page(url)
    # get_content(html)


if __name__ =='__main__':
    main()
