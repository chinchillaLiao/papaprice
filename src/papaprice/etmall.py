import re
import requests
import json
import js2py
from bs4 import BeautifulSoup as bs 
from papaprice.papaprice import PapaPrice

        
class Etmall(PapaPrice):
    def __init__(self, proxies = None):
        super().__init__(proxies)
        self.url_template = 'https://www.etmall.com.tw/i/{}'
        
    def _parse(self, response):
        name = None
        price = None
        soup = bs(response.text, 'html.parser')
        script = soup.find('script', string = re.compile("'ViewContent'")).string
        script = script.replace('\r',' ').replace('\n',' ')
        content = re.search("(?<='ViewContent',)[^}]+}",script)[0]
        js = js2py.eval_js('js=' + content)
        name = js['content_name']
        price = js['value']
        return name, price

        

        
        