import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_DOMAIN, PEP_URL, SPIDER_NAME

PATTERN = r'(?P<number>\d+).–.(?P<name>.*)'


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = [PEP_DOMAIN, ]
    start_urls = [PEP_URL]

    def parse(self, response):
        for link in response.css(
                '#numerical-index a.pep.reference.internal::attr(href)'
        ).getall():
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = re.search(
            PATTERN, response.css('h1.page-title::text').get()
        ).groups()
        yield PepParseItem(
            number=number,
            name=name,
            status=response.css('dt:contains("Status") + dd abbr::text').get()
        )
