import scrapy


class FlatsSpider(scrapy.Spider):
    name = "flats"
    start_urls = [
	'http://diesel.elcat.kg/lofiversion/index.php?f459-0.html'
    ]

    def parse(self, response):
        for flat in response.css('div.topicwrap li'):
            yield {
                'title': flat.css('a::text').extract_first(),
                'link': flat.css('a::attr(href)').extract_first(),
            }
