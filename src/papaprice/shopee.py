import re
import requests
import json
import js2py
from bs4 import BeautifulSoup as bs 
from papaprice.papaprice import PapaPrice


        
class Shopee(PapaPrice):
    def __init__(self, proxies = None):
        super().__init__(proxies)
        self.url_template = 'https://shopee.tw/api/v2/item/get?itemid={}&shopid={}'
        
    def _url(self, i_code):
        shopid, itemid  = i_code.split('.')
        url = self.url_template.format(str(itemid), str(shopid))
        return url 
        
    def _request(self, i_code):
        url = self._url(i_code)
        headers = self._headers({'referer': f'https://shopee.tw/--i.{i_code}'})
        proxies = self._proxies()
        response = requests.get(url, headers = headers, proxies = proxies, timeout = 10)
        return response
        
    def _parse(self, response):
        name = None
        price = None
        dct = response.json()
        name = dct['item']['name']
        price = dct['item']['models'][0]['price']
        price = int(price/100000)
        return name, price

        

        
        