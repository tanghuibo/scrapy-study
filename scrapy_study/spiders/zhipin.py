# -*- coding: utf-8 -*-
import scrapy

from scrapy_study.items import ZhipinScrapyItem
from scrapy_study.uitls.csvMaker import CsvMaker


class ZhipinSpider(scrapy.Spider):

    scvMaker = CsvMaker("result.csv", ['job', 'money', 'desc', 'url'])
    name = "zhipin"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["https://www.zhipin.com/gongsir/5d627415a46b4a750nJ9_100000.html?page=1&ka=page-1"]

    def parse(self, response):
        job_list = response.xpath("//div[@class='job-list']/ul/li")
        for job in job_list:
            item = ZhipinScrapyItem()
            item['job'] = job.xpath(".//div[@class='job-title']/text()").extract_first()
            item['money'] = job.xpath(".//div[@class='title-box']/span[@class='red']/text()").extract_first()
            item['desc'] = job.xpath(".//div[@class='job-primary']/div[@class='info-primary']/p/text()").extract_first()
            item['url'] = job.xpath(".//a/@href").extract_first()
            self.scvMaker.add(item)
        next = response.xpath("//div[@class='page']/a[@class='next']/@href").extract()
        if next:
            yield scrapy.Request("https://www.zhipin.com" + next[0], callback=self.parse)
        pass
