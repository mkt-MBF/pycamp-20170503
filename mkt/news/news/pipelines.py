# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import psycopg2


class NewsPipeline(object):
    def process_item(self, item, spider):
        return item


class YahooPipeLine:
    #データベース接続
    def open_spider(self, spider):
        self._conn = psycopg2.connect( "dbname='pycamp_201705' user='pycamp' host ='localhost' password='pycamp'" )
        self._cur = self._conn.cursor()
    
    #アイテムのデータベスへの登録
    def process_item(self, item, spider):
        print( len(item['date']), len(item['ttl']), len(item['cate']),len(item['link']) )
        
        for i in range( len(item['cate']) ):
            if len(item['link']) < len(item['cate']):
                self._cur.execute( "insert into news (date, title, category, link ) values (%s, %s, %s, %s);", ( item['date'][i], item['ttl'][i], item['cate'][i], "" ) )
        
            else:
                self._cur.execute( "insert into news (date, title, category, link ) values (%s, %s, %s, %s);", ( item['date'][i], item['ttl'][i], item['cate'][i], item['link'][i] ) )
        self._conn.commit()
        return item

    #データベースへの接続解除
    def close_spider(self, spider):
        pass
