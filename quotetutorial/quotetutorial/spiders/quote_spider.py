import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    
    # ! DONT CHANGE THE NAME OF THESE TWO VARIABLES (NAME AND URLS),
    # ! BECAUSE SCRAPY.SPIDER CLASS EXPECTS US TO HAVE THESE TWO WITH SAME NAME.

    # name of the spider.
    name =  'quotes'

    # list of urls that spider will scrape.
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # The response will contain the source code of website.

        # Creating the instance of items.py
        items = QuotetutorialItem()

        # Scraping titles, authors and tags from source code.
        all_div_quotes = response.css('div.quote')  

        for quote in all_div_quotes:
            titles = quote.css('span.text::text').extract()
            authors = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()

            items['title'] = titles
            items['author'] = authors
            items['tag'] = tags

            yield items