# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data in temporary containers (items) then storing in database.

import scrapy


class QuotetutorialItem(scrapy.Item):

    # temporary continers called fields.
    title = scrapy.Field() 
    author = scrapy.Field()
    tag = scrapy.Field()
