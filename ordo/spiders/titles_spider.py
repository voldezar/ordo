import scrapy


class FlatsSpider(scrapy.Spider):
    name = "flats"
    start_urls = ["http://diesel.elcat.kg/index.php?showforum=459"]

    def parse(self, response):
        pages = response.xpath('//li[@class="next"]/a/@href').extract_first()
        for page in pages:
            yield scrapy.Request(page, callback=self.parse_page)
            
    def parse_page(self, response):
        flats = response.xpath('//td[@class="col_f_content "]')
        for flat in flats:
            yield {
                'title': flat.xpath('h4/a/span/text()').extract_first(),
                'link': flat.xpath('h4/a/@href').extract_first(),
#                'price': flat.xpath('h4/a/span/text()').re('\d{3-7}\$?'),
#                'description': scrapy.Request(flat, callback=self.parse_description)
            }

#    def parse_description(self, response):
#        description = response.css('div.postcontent::text').extract_first()

