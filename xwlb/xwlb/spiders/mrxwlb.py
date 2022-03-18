import scrapy
import re
import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# from xwlb.xwlb.items import XwlbItem
from ..items import XwlbItem


class MrxwlbSpider(scrapy.Spider):
    name = 'mrxwlb'
    allowed_domains = ['xwlb.com.cn']
    base_urls = 'http://www.xwlb.com.cn/'
    start_urls = ['http://www.xwlb.com.cn/cctv.html']
    rules = [Rule(LinkExtractor(allow=['/\d+\.html']), 'parse')]

    def detailParse(self, response):
        item = response.meta['item']
        text = response.xpath("//div[@class='single']/p")
        res = ""
        for t in text:
            if t.xpath('.//strong/a/text()').extract():
                res += '|'
            res += str(t.xpath('.//text()').extract_first()).strip()
        item['details'] = res
        return item

    def parse(self, response):
        """
        解析 title,date,details,summary
        """
        text = response.xpath("//div[@class='post item']")
        for t in text:
            item = XwlbItem()
            title = t.xpath('.//h2/a/text()').extract_first()
            entitle = str(title).strip()
            numpattern = re.compile(r"\d+")
            nums = numpattern.findall(entitle)
            if len(nums) == 3:
                item['date'] = datetime.date(int(nums[0]), int(nums[1]),
                                             int(nums[2]))
            else:
                item['date'] = entitle
            summary = t.xpath(
                ".//div[@class='intro isimg']/text()").extract_first()
            ensummary = str(summary).strip()

            item['title'] = entitle
            item['summary'] = ensummary
            next = t.xpath(".//h2/a/@href").extract_first()
            url = response.urljoin(next)
            yield scrapy.Request(url=url,
                                 meta={'item': item},
                                 callback=self.detailParse)
            # item['details'] = str(details).strip()
            # yield item

        # next = response.xpath("//div[@class='pagebar']/span[@class='next-page']/a/@href").extract_first()

        # url = response.urljoin(next)
        # yield scrapy.Request(url=url, callback=self.parse)
