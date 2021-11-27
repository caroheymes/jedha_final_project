import scrapy
import pandas as pd
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import JobItem
import json
from scrapy.loader import ItemLoader


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    # allowed_domains = ['anpe.com']

    my_file = 'C:/Users/carol/Documents/jobs/scrap/scrap/no_top10_links.csv'
    df = pd.read_csv(my_file)
    my_list = df.link.values.tolist()

    start_urls = my_list
    
    def parse(self, response):
    #     # Old stuff to check xpath
    #     items = {
    #     # 'raw_url'           :response.url,
    #     # 'meta_desc'         : response.xpath('/meta[@name="description"]/@content').get(),
    #     # 'h1'                : response.xpath('//h1/text()').get(),
    #     'content'           : response.xpath('//body/..//p/text() | //body/..//li/text()  | //body/..//div/text() | //body/..//span/text() | //body/..//section/text()').getall(),
    #     }
    #     yield items
                    
        #On instancie ItemLoader pour faciliter le cleaning
        l= ItemLoader(item= JobItem(), response = response)
        
        l.add_value('raw_url', response.url)
        l.add_xpath('title', '//title/text()')
        l.add_xpath('meta_desc', '/meta[@name="description"]/@content')
        l.add_xpath('h1', '//h1/text()')
        l.add_xpath('h2', '//h2/text()')
        l.add_xpath('h3',  '//h3/text()')
        l.add_xpath('h4',  '//h4/text()')
        l.add_xpath('canonical',  '//link[@rel="canonical"]/@href')
        l.add_xpath('nav_links_text', '//nav//a/text()')
        l.add_xpath('header_links_text',  '//header//a/text()')
        l.add_xpath('header_links_href', '//header//a/@href')
        l.add_xpath('content',  '//body/..//p/text() | //body/..//li/text()  | //body/..//div/text() | //body/..//span/text() | //body/..//section/text()')
        # l.add_xpath('content2',  '//body/..//p/text() | //body/..//li/text()  | //body/..//div/text() | //body/..//span/text() | //body/..//section/text()')
       
       
        yield l.load_item()

