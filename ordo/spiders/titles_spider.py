import scrapy


class FlatsSpider(scrapy.Spider):
    name = "flats"
    start_urls = [
	'http://diesel.elcat.kg/lofiversion/index.php?f459.html'
    ]

    def parse(self, response):
        pages = response.css('div.ipbpagespan a::attr(href)').extract()
        for page in pages:
            yield scrapy.Request(page, callback=self.parse_page)
            
    def parse_page(self, response):
        flats = response.css('div.topicwrap li')
        for flat in flats:
            yield {
                'title': flat.css('a::text').extract_first(),
                'link': flat.css('a::attr(href)').extract_first(),
                'price': flat.css('a::text').re('\d+\$'),
            }
