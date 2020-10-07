# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json
from scrapy.linkextractors import LinkExtractor

class TransferSpider(scrapy.Spider):
    name = "transfer_prices"
    
    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }

    start_urls = ['https://www.transfermarkt.co.uk/transfers/saisontransfers/statistik?land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&transferfenster=&saison-id=2020&plus=1']
    

    def parse(self, response):
        for i in range(1, 50):
            path = "/html/body/div[2]/div[8]/div[1]/div/div[3]/div/table/tbody/tr[{}]//text()".format(i)
            #player_name = response.xpath("/html/body/div[2]/div[8]/div[1]/div/div[3]/div/table/tbody/tr[1]//text()")[9].get()
            #player_str = "/html/body/div[2]/div[8]/div[1]/div/div[3]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[{}]/td[2]/a".format(i)
            # player_url = response("/html/body/div[2]/div[8]/div[1]/div/div[3]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[2]/a").get()
            try:
                yield { 
                    'player_name' : response.xpath(path)[9].extract(),
                    'position' : response.xpath(path)[14].extract(),
                    'age' : response.xpath(path)[18].extract(),
                    'transfermarkt_val' : response.xpath(path)[19].extract(),
                    'team_left' : response.xpath(path)[26].extract(),
                    'league_left' : response.xpath(path)[33].extract(),
                    'joined_team' : response.xpath(path)[44].extract(),
                    'joined_league': response.xpath(path)[51].extract(),
                    'fee': response.xpath(path)[56].extract()
                    
                    }
            except:
                pass
        next_page = response.xpath("/html/body/div[2]/div[8]/div[1]/div/div[3]/div/div[2]/ul/li[13]/a//@href").get()
        #next_page = response.xpath("/html/head/link[42]//@href")[0].extract()
        # next_page= response.xpath("/html/head/link[42]").get()
        url_str = ''.join(map(str, next_page))     #coverts list to str
        
        #yield response.follow(next_page, self.parse)
        
        

        #yield response.follow(next_page, self.parse)
       #response.xpath("/html/head/link[42]")
       # cd  
       # response.xpath("/html/body/div[2]/div[8]/div[1]/div/div[3]/div/div[2]/ul/li[13]/a")