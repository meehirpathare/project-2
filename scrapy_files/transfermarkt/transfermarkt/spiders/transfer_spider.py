# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json

class TransferSpider(scrapy.Spider):
    name = "transfer_prices"
    
    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }

    start_urls = ['https://www.transfermarkt.co.uk/transfers/saisontransfers/statistik?land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&transferfenster=&saison-id=2020']

    def parse(self, response):
        for i in range(1, 26):
            path = "/html/body/div[2]/div[8]/div[1]/div/div[3]/div/table/tbody/tr[{}]//text()".format(i)
        # player_name = response.xpath("/html/body/div[2]/div[8]/div[1]/div/div[3]/div/table/tbody/tr[1]//text()")[9].get()    
            #player_name = response.xpath(path)[9].get()
            yield {
                'player_name' :  response.xpath(path)[9].get()
                }
        