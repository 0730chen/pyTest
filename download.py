# from time import time
# from threading import Thread
# import requests

# class Download(Thread):
#     def __init__(self,url):
#         super().__init__
#         self.url = url
#     def run(self):
#         filename = self.url[self.url.rfind('/')+1:]
#         resp = requests.get(self.url)
#         with open('../pyL/__pycache__/hao'+filename, 'wb') as f:
#             f.write(resp.content)

# def main():
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#     url = 'https://uploadbeta.com/api/pictures/random/?key=BingEverydayWallpaperPicture'
#     r = requests.get(url,headers = headers)
#     # resp = requests.get('https://uploadbeta.com/api/pictures/random/?key=BingEverydayWallpaperPicture',headres=headers)
#     # r.encoding = 'utf-8'
   
#     print(r)
#     # data_model = resp.json()
#     # for mm_dict in data_model['newslist']:
#     #     url = mm_dict['picUrl']
#     #     Download(url).start()
# if __name__ =='__main__':
#     main()
