import scrapy

'''
95598新疆停电公告
'''
class PowerOutageSpider(scrapy.Spider):
    name = 'power_outage'
    # allowed_domains = ['www.111.com']
    start_urls = ['https://osg-web.sgcc.com.cn/osgweb/index']

    def parse(self, response):
        pass
        # return res
