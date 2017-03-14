import scrapy


class FlatsSpider(scrapy.Spider):
    name = "flats"
    start_urls = ['http://diesel.elcat.kg/index.php?showforum=459']

    def parse(self, response):
        flats = response.xpath('//td[@class="col_f_content "]')
        for flat in flats:
            yield {
                'title': flat.xpath('h4/a/span/text()').extract_first(),
                'link': flat.xpath('h4/a/@href').extract_first(),
                'price': flat.xpath('h4/a/span/text()').re('\d{3-7}\$?'),
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
