# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class TransferSpider(scrapy.Spider):
    name = "transfers"
    start_urls = [
        'https://www.transfermarkt.co.uk/transfers/saisontransfers/statistik?land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&transferfenster=&saison-id=2020&'
    ]

    def parse(self, response):
        page = response.url
        filename = '2020_test.html'
        with open(filename, 'wb') as f:
            f.write(response.body)