import json
import scrapy
import random
from fake_useragent import UserAgent
from earthquake.items import EarthquakeItem

'''main'''
class earthquakeSpider(scrapy.Spider):
    name = 'earthquake'
    ua = UserAgent()

    def start_requests(self):
        for i in range(1, 346):
            headers = {'user-agent': self.ua.random}
            yield scrapy.Request(r'http://www.ceic.ac.cn/ajax/search?page={i}&&start=2000-01-01&&end=2019-06-24&&jingdu1=&&jingdu2=&&weidu1=&&weidu2=&&height1=&&height2=&&zhenji1=&&zhenji2=&&callback=jQuery18009715921827266145_1561344231300&_=1561344243644', headers=headers)

    def parse(self, response):
        for i in json.loads((response.text)[41: -1]).get('shuju'):
            item = EarthquakeItem()
            item['level'] = i.get('M')
            item['o_time'] = i.get('O_TIME')
            item['latitude'] = i.get('EPI_LAT')
            item['longitude'] = i.get('EPI_LON')
            item['depth'] = i.get('EPI_DEPTH')
            item['location'] = i.get('LOCATION_C')
            yield item