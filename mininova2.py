# -*- coding: utf-8 -*-
import scrapy
import numpy
from scrapy.http.request import Request
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.response import open_in_browser
from mininova2_spider.items import Mininova2SpiderItem


class Mininova2Spider(scrapy.Spider):
    name = "mininova2_spiderl"
    allowed_domains = ["mininova.org"]
    #start_urls = ['http://www.mininova.org/tor/13364426']
    
    test =  numpy.arange(13364426, 13364428, 1)
    iter = numpy.arange(0, len(test), 1)
    start_urls = []

    for i in iter:
        start_urls.append("http://www.mininova.org/tor/" + str(test[i]) + "/")    
    print(start_urls)
                                          
    def parse(self, response):
        torrent = Mininova2SpiderItem('')
        torrent["title"] = response.xpath("//div[@id='content']/h1/text()").extract()
        print(torrent["title"])
        torrent["size"] = response.xpath("//div[@id='specifications']/p[2]/text()[2]").extract()
        print(torrent["size"])
        torrent["language"] = response.xpath("//div[@id='specifications']/p[4]/text()[3]").extract()
        print(torrent["language"])
        #open_in_browser(response) # öffnet den Browser, mit der url nach der gecrawled wird
        yield(torrent)
                                    


    #def parse(self, response):
    #    yield FormRequest.from_response(response,
    #                                      formnumber=1,
    #                                      formxpath='id("searchform")',
    #                                      formdata={'searchTerm': 'love'},
    #                                      callback=self.parse1, method="GET")