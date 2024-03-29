import scrapy
from scrapy.spiders import Spider
from acg.items import ImageItem

class blogSpider(Spider):
	name="blog"
	start_urls = ["http://www.acg.fi/anime/page/1"]
	page = 1
	count = 0
	MAX_CATCH_PAGES = 100
	item = ImageItem()
	
	def parse(self,response):
		pages = response.xpath('//*[@id="main"]//a//@href').re(r'https://acg.fi/anime/([0-9]+)\.htm')
		used = []
		for page in pages:
			if page not in used:
				used.append(page)
		print('find %d secound pages' %len(used))
		for number in used:
			url = "http://www.acg.fi/anime/%s.htm" % number
			self.item['url'] = url
			yield scrapy.Request(url, callback=  self.post_page)
		if self.page < self.MAX_CATCH_PAGES:
			self.page = self.page+1
			next_url = "http://www.acg.fi/anime/page/%d" % self.page
			yield scrapy.Request(next_url,callback = self.parse)
	def post_page(self, response):
		
		images_url =  response.xpath('//*[@id="post-single"]/header/div[1]').extract()
		for i in images_url:
			img_url = i[49:-10]
			img_urls = []
			# print('获取到页面数量%d'len(img_url))
			# print('find %d images' %len(img_url))
			if img_url[1] == '/':
				img_url = img_url[2:-1] + 'j'
			else:
				img_url = img_url

			img_urls.append(img_url)
			print('获取到%d图片'%len(img_urls))
			self.item['image_urls'] = img_urls
			print('我是最终的item数据',self.item)
			return self.item
				
			
			
