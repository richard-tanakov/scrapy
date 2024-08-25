import scrapy


class TestLinksSpider(scrapy.Spider):
    name = "test_links"
    allowed_domains = ["rss.app"]
    start_urls = ["https://rss.app/feeds/K8NaxkgaFm2oQHgI.xml"]

    def parse(self, response):
        for links in response.xpath('//item'):
            yield {'link': links.xpath('.//link/text()').get()} 
