# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinScrapyItem(scrapy.Item):
    # 职务
    job = scrapy.Field()
    # 薪酬
    money = scrapy.Field()
    # 链接
    url = scrapy.Field()
    # 描述
    desc = scrapy.Field()
    pass
