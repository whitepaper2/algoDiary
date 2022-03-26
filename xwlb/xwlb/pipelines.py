# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymysql
import redis


class XwlbPipeline:
    def process_item(self, item, spider):
        return item


class TextPipeline(object):
    def __init__(self) -> None:
        self.rmchar = '|'

    def process_item(self, item, spider):
        if item['summary']:
            item['summary'] = item['summary'][:100]
        if item['details']:
            item['details'] = item['details'][1:-1]
            return item
        else:
            return DropItem("Missing Text")


class DuplicatePipeline(object):
    def open_spider(self, spider):
        host = spider.settings.get('REDIS_HOST', 'localhost')
        port = spider.settings.get('REDIS_PORT', 6379)
        self.redis_db = redis.Redis(host=host, port=port)
        self.data_key = 'xwlbdate'

    def close_spider(self, spider):
        self.redis_db.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        dup = 'xwlb'+item['date']
        # print(self.redis_db,dup)
        if self.redis_db.sismember(self.data_key,dup):
            return DropItem("Duplicate Text")
        else:
            self.redis_db.sadd(self.data_key,dup)
            return item
        


class MySQLPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'spider')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'spiderman')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'spiderman1234')

        self.db_conn = pymysql.connect(host=host,
                                       port=port,
                                       db=db,
                                       user=user,
                                       passwd=passwd,
                                       charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = (
            item['date'],
            item['title'],
            item['summary'],
            item['details'],
        )

        sql = 'INSERT INTO xwlb(date,title,summary,details) VALUES(%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)