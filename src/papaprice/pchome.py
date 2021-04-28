import re
import requests
import json
import js2py
from bs4 import BeautifulSoup as bs 
from papaprice.papaprice import PapaPrice

        
class Pchome(PapaPrice):
    def __init__(self, proxies = None):
        super().__init__(proxies)
        self.url_template = 'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{}&fields=Seq,Id,Name,Price&_callback=jsonp_prod&1619356140?_callback=jsonp_prod'
    
    def _parse(self, response):
        name = None
        price = None
        dct = json.loads(response.text[15:-48])
        item = list(dct.values())[0]
        name = item['Name']
        price = item['Price']['P']
        return name, price

        

        

        
        