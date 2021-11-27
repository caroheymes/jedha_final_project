# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_comments, remove_tags, replace_escape_chars,strip_html5_whitespace,get_base_url
import re
from unidecode import unidecode


class JobItem(scrapy.Item):

    # #Suppression des sauts de lignes éventuels
    def stripn(x):
        x = unidecode(x)
        x = re.sub('\s{2,10000}',  ' ', x)
        x = remove_tags(x)
        x = strip_html5_whitespace(x)
        x = replace_escape_chars(x)
        trans_table = {ord(c): None for c in u'\r\n\t'}
        x =  ''.join(x.strip().translate(trans_table))
        x = re.sub('\s{2,10000}',  ' ', x)
        x = re.sub('@{3,2000}',  '', x)
        x = x.replace('@@@', '@@')
        return x


    def filter_empty(x):
        if x != '' :
            return x

    def special_join(my_list):
        my_list = [x for x in my_list if x] 
        return ' '.join(my_list)

    # def another_special_join(my_list):
    #     my_list = [x for x in my_list if x] 
    #     return ' '.join(my_list)
    
        

    
    raw_url = scrapy.Field(
        input_processor = MapCompose(replace_escape_chars),
        output_processor = TakeFirst()
                            )

    title = scrapy.Field(
        input_processor = MapCompose(stripn),
        output_processor = TakeFirst()
                            )
    meta_desc = scrapy.Field(
    input_processor = MapCompose(stripn,filter_empty ),
    output_processor = Join('@@')
                            )
    h1 = scrapy.Field(
    input_processor = MapCompose(stripn, filter_empty, ),
    output_processor = TakeFirst()
                            )
    h2 = scrapy.Field(
    input_processor = MapCompose(stripn, filter_empty),
    output_processor = Join('@@')
                            )
    h3= scrapy.Field(
    input_processor = MapCompose(stripn, filter_empty),
    output_processor = Join('@@')
                    )

    h4 = scrapy.Field(
    input_processor = MapCompose(stripn, filter_empty),
    output_processor = Join('@@')
                    )

    canonical = scrapy.Field(
    input_processor = MapCompose(stripn, filter_empty),
    output_processor = TakeFirst()
                            )

    nav_links_text = scrapy.Field(
    input_processor = MapCompose(stripn, filter_empty),
    output_processor = Join('@@')
                                )
    
    header_links_text = scrapy.Field(
    input_processor = MapCompose(stripn, filter_empty),
    output_processor = Join('@@')
                                    )
    
    header_links_href = scrapy.Field(
    input_processor = MapCompose(stripn, filter_empty),
    output_processor = Join('@@')
                                    )

    content = scrapy.Field(
    input_processor = MapCompose(stripn, 
                                filter_empty
                                # filter_space, special_join
                                ),
    output_processor = Join()
                             )
    # content2 = scrapy.Field()
  