# import sys
# print(sys.version)
# 路徑：C:\user\Anaconda3\envs\scrapyTest\Lib\site-packages\scrapy\booksDemo
# import sys
# import io
import scrapy
# from urllib import parse as urlparse
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
class quote(scrapy.Item):
    content = scrapy.Field()
    source = scrapy.Field()
    author = scrapy.Field()

class booksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.com.tw"]
    start_urls = [
        "http://activity.books.com.tw/everylettermatters/sentence/latest"
    ]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
        # learn_nodes = response.css('div.item')
        learn_nodes = response.xpath('//div[@class="item"]')
        for learn_node in learn_nodes:
            item = quote()
            item['content'] = "".join(str(learn_node.css('h5 > a::text').extract_first()).split())
            item['source'] = learn_node.css('p.source-book>span.link>a::text').extract_first()
            item['author'] = str(learn_node.css('p.source-book>span.link:nth-child(2) >a::text').extract_first())
            yield item
            # yield{
            #     'content：' : "".join(str(learn_node.css('h5 > a::text').extract_first()).split()) ,
            #     'source:' : learn_node.css('p.source-book>span.link>a::text').extract_first(),
            #     'from :' : str(learn_node.css('p.source-book>span.link:nth-child(2) >a::text').extract_first())
            #     # '來源：' : learn_node.css('p.source-book>span.link>a::text').extract_first(),
            #     # '作者：' : learn_node.css('p.source-book>span.link:nth-child(2) >a::text').extract_first()
            # }
