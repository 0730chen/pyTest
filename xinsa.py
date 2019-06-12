import requests
from bs4 import BeautifulSoup
import json

cookie = 'SINAGLOBAL=1488887630751.4941.1531449151189; UM_distinctid=167ba982dfd280-07b9dd87197018-3764460c-1fa400-167ba982dfe338; login_sid_t=b86fc933ae598b2e75c475ec1a5d7faf; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=8707730994720.546.1548040189349; ULV=1548040189357:9:5:1:8707730994720.546.1548040189349:1547892183663; WBtopGlobal_register_version=84a7c082648185f6; YF-V5-G0=f0aa2e6d566ccd1c288fae19df01df56; un=18402910015; Ugrow-G0=e1a5a1aae05361d646241e28c550f987; wb_view_log_5481009706=1920*10801; wb_view_log=1920*10801; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFvBT2Z_an6W7s7C6l2UYP55JpX5K2hUgL.Fo-X1h27eh.Nehq2dJLoIXjLxKqL1hnL1K2LxKqL1KnLB-qLxKMLBK-L1KqLxK-L1-zLB.BLxKML1-2L1hBLxKML1h.L1-zLxKMLBozLB-2LxK-L1K2L1hWHUH-t; ALF=1591841096; SSOLoginState=1560305097; SCF=AtKofbp8us-5rDa562EFgUriaO5uEO4NE3Yr7dZ5ADKQYzAYJgZzdGYBziQkmDQZTIO7kH3v8Y7rwv0PSB223SE.; SUB=_2A25wBC2ZDeRhGeNK41MR8CfLyzqIHXVTcBhRrDV8PUNbmtBeLVP8kW9NSVyELwKZ1Xr32xEI8SIZ8ONeh5JhS9KT; SUHB=0Jvg4KovgagMCw; wvr=6; webim_unReadCount=%7B%22time%22%3A1560324193994%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A12%2C%22msgbox%22%3A0%7D; YF-Page-G0=f1e19cba80f4eeaeea445d7b50e14ebb|1560324202|1560324202'

def get_html(url):
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",'cookie':cookie}
    r = requests.get(url,headers = headers)
    # print(type(r))
    # print(r.json()['data'])
    # r.encoding = 'utf-8'
    return r.json()['data']
def get_content(html):
    soup = BeautifulSoup(html,'lxml')
    weiboList = soup.find_all('div',attrs={'nick-name':'皮卡丘的皮喽'})
    # print(weiboList)
    # print(soup)
    # weiboList = soup.find_all('div',id='Pl_Official_MyProfileFeed__21')
    Contents = []
    for web in weiboList:
        webLs={}
        # try:
        # print(web)
        webLs['title'] = web['nick-name']
        # #使用.text.strip()获取标签内容
        webLs['content'] = web.text.strip()
        
        img = web.find_all('img',attrs={'render':'ext'})
        for imgs in img:
            webLs['imgUrl'] = imgs['src']
            webLs['imgContent'] = imgs['title']
        Contents.append(webLs)
        # print(Contents)
    # print(Contents)
    return Contents
        # print(webLs)
   
    # return webLs
        
    # Contents.append(webLs)
    # # print(Contents)
    # print(Contents)
    # return Contents
    
        
            
        # print(img)
        # print(web)
        # print(img)
        # if(img == 'None'):
        #     print('这个img是空的')
        # else:
        #     print('不是空的img'+img)
            # print(img['src'])
            # webLs['imgContent'] = web.find_all('img')['alt']
        # print(type(img))
        # print(web)
        # print(img)
        # webLs['imgContent'] = web.find_all('img')['alt']
        # webLs['imgUrl'] = web.find_all('img')['src']
        # Contents.append(webLs)
        # except:
        #     print('有问题')
        # return Contents
        
        


    # print(soup)
    # weiboList = soup.find_all(attrs={'class':'WB_feed WB_feed_v3 WB_feed_v4'})
    # print(type(weiboList))
    # print(weiboList)
    # for weibo in weiboList:
    #     # print(type(weiboList))
    #     print(type(weibo))
        # weibos = weibo.find_all(class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_like ')
        # print(weibos)
        
        # print(type(weibo))
        # print(weibo)
    # weiboList = soup.find_all('div')
    # print(type(soup))
    # # print(soup)
    # print(type(weiboList))
    # print(weiboList)
def save(data):
    with open('weibo.text','a+',encoding="utf-8") as f:
        # print(str(data))
        # f.write(str(data))
        # print(json.dumps(data))
        for content in data:
            # print(str(content))
            
            # f.write(json.dumps(content))
            print('正在保存内容')
            f.write(str(content))
            
            # titles = "名称：{} \n 内容: {} 表情{}\n 表情链接{}------------\n"
            # f.write(content)
            # f.write(titles.format(content['title'],content['content'],content['imgContent'],content['imgUrl']))

def main():
    url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&topnav=1&wvr=6&topsug=1&is_all=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__21&id=1005055719553230&script_uri=/u/5719553230&feed_type=0&page=1&pre_page=1&domain_op=100505&__rnd=1560318395223'
    html = get_html(url)
    # print(html)
    Contents = get_content(html)
    print('成功获取网页内容')
    save(Contents)
    print('保存成功')
    
if __name__ == '__main__':
    main()