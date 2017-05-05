import scrapy


class SpiderName(scrapy.Spider):
    name = 'yahoo'
    start_urls = ['https://news.yahoo.co.jp/list/',]
    base_url = 'https://news.yahoo.co.jp'

    def parse( self, response ):

        # 月/日(曜) 時:分
        date = response.css('span.date ::text').extract()
        print(date)
        
        # 記事タイトル
        ttl = response.css('span.ttl ::text').extract()
        print(ttl)
        
        # カテゴリー
        cate = response.css('span.cate ::text').extract()
        print(cate)
        
        # 記事本体URL
        link = response.css('ul.list li a::attr(href)').extract()
        print(link)
        
        # 次ページURL (リスト!!!!)
        next_page = response.css('li.next a::attr(href)').extract()
        print(next_page)
        
        
        yield date, ttl, cate, link, next_page



        if next_page:
            # 次ページURL生成　next_pageは、リスト！
            yield scrapy.Request(url= 'https://news.yahoo.co.jp' + str( next_page[0] ) )

