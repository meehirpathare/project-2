# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from urllib.request import urlopen

class TransferSpider(scrapy.Spider):
    name = "transfer_prices"
    year = scrapy.Field()
    year = 2020
    
    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURENT_REQUESTS_PER_DOMAIN": 1,
        "HTTPCACHE_ENABLED": False
    }
      
    start_urls = ['https://www.transfermarkt.co.uk/transfers/saisontransfers/statistik?land_id=0&ausrichtung=Torwart&spielerposition_id=&altersklasse=&leihe=&transferfenster=alle&saison-id={}&plus=1'.format(year),
                  'https://www.transfermarkt.co.uk/transfers/saisontransfers/statistik?land_id=0&ausrichtung=Abwehr&spielerposition_id=&altersklasse=&leihe=&transferfenster=alle&saison-id={}&plus=1'.format(year),
                  'https://www.transfermarkt.co.uk/transfers/saisontransfers/statistik?land_id=0&ausrichtung=Mittelfeld&spielerposition_id=&altersklasse=&leihe=&transferfenster=alle&saison-id={}&plus=1'.format(year),
                  'https://www.transfermarkt.co.uk/transfers/saisontransfers/statistik?land_id=0&ausrichtung=Sturm&spielerposition_id=&altersklasse=&leihe=&transferfenster=alle&saison-id={}&plus=1'.format(year)
                  #'https://www.transfermarkt.co.uk/transfers/saisontransfers/statistik?land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&transferfenster=&saison-id={}&plus=1'.format(year)
                  ]
    
    def parse(self, response):
        for i in range(1, 26):
             path = "/html/body/div[2]/div[8]/div[1]/div/div[3]/div/table/tbody/tr[{}]//text()".format(i)
             
             n = 7*i - 4
             url_path = "/html/body/div[2]/div[8]/div[1]/div/div[3]/div/table//a//@href"
             base_url = "https://www.transfermarkt.co.uk"
             
            
             try:
                 yield {
                       'year' : self.year,
                       'player_name' : response.xpath(path)[9].extract(),
                       'position' : response.xpath(path)[14].extract(),
                       'age' : response.xpath(path)[18].extract(),
                       'transfermarkt_val' : response.xpath(path)[19].extract(),
                       'team_left' : response.xpath(path)[26].extract(),
                       'league_left' : response.xpath(path)[33].extract(),
                       'joined_team' : response.xpath(path)[44].extract(),
                       'joined_league': response.xpath(path)[51].extract(),
                       'fee': response.xpath(path)[56].extract(),
                       'url' : base_url + response.xpath(url_path)[n].get()
                       }
             except:
                 pass

        next_page = response.xpath("/html/body/div[2]/div[8]/div[1]/div/div[3]/div/div[2]/ul/li[13]/a//@href").get()
        
        if next_page is not None:
            yield response.follow(next_page, self.parse)
          
           