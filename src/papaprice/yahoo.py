import re
import requests
import json
import js2py
from bs4 import BeautifulSoup as bs 
from papaprice.papaprice import PapaPrice



class Yahoo(PapaPrice):
    def __init__(self, proxies = None):
        super().__init__(proxies)
        self.url_template = 'https://tw.buy.yahoo.com/gdsale/gdsale.asp?gdid={}'
        
    def _parse(self, response):
        name = None
        price = None
        soup = bs(response.text, 'html.parser')
        s = soup.find('script', attrs = {'type':"application/ld+json"}).string
        dct = json.loads(s)
        name = dct[1]['name']
        price = dct[0]['offers']['price']
        price = int(price)
        return name, price
        
        

        

        
        