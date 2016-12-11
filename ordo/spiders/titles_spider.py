import scrapy


class QuotesSpider(scrapy.Spider):
    name = "links_sell_1k"
    start_urls = [
	'http://diesel.elcat.kg/lofiversion/index.php?f459-0.html'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

            response.xpath('//div[@id="ipbcontent"]//a/text()').extract()
            response.xpath('//div[@id="ipbcontent"]//a/@href').extract()
