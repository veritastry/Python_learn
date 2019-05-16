# -*- coding: utf-8 -*-
import scrapy
from collectips.items import CollectipsItem

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def start_requests(self):
    	reqs = []

    	for i in range(1, 5):
    		req = scrapy.Request("http://www.xicidaili.com/nn/%s"%i)
    		reqs.append(req)

    	return reqs

    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]')

        trs = ip_list[0].xpath('tr')

        items = []

        for ip in trs[1:]:
        	pre_item = CollectipsItem()
        	pre_item['ip'] = ip.xpath('td[2]/text()')[0].extract()
        	# pre_item['position'] = ip.xpath('td[4]/a/text()')[0].extract()
        	pre_item['port'] = ip.xpath('td[3]/text()')[0].extract()
        	pre_item['ip_type'] = ip.xpath('td[6]/text()')[0].extract()
        	pre_item['speed'] = ip.xpath('td[7]/div[@class="bar"]/@title')[0].extract()
        	pre_item['last_check_time'] = ip.xpath('td[10]/text()')[0].extract()
        	items.append(pre_item)

        return items

