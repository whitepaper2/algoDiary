# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class XwlbPipeline:

    def process_item(self, item, spider):
        return item


        # if item['details']:
class TextPipeline(object):

    def __init__(self) -> None:
        self.rmchar = '|'

    def process_item(self, item, spider):
        if item['details']:
            item['details'] = item['details'][1:-1]
            return item
        else:
            return DropItem("Missing Text")
