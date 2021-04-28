import re
import requests
import json
import js2py
from bs4 import BeautifulSoup as bs 
from papaprice.papaprice import PapaPrice


class Momo(PapaPrice):
    def __init__(self, proxies = None):
        super().__init__(proxies)
        self.url_template = 'https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code={}'

    def prod_name(self, x):
        return x.name == 'h3' and x.get('id') is None and x.findChild() is None
        
    def prod_price(self, x):
        if x.name == 'span' and x.get('id') is None and not x.has_attr('class') and x.string:
            parent = x.find_parent()
            if parent.name == 'li':
                if parent.has_attr('class'):
                    if parent['class'][0] == 'special':
                        return True
        return False
            
    def _parse(self, response):
        name = None
        price = None
        soup = bs(response.text, 'html.parser')
        name = soup.find(self.prod_name).string
        price = soup.find(self.prod_price).string
        price = int(price.replace(',',''))
        return name, price

        


        

        
        