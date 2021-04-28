import re
import requests
import json
import js2py
from bs4 import BeautifulSoup as bs 


class PapaPrice():
    def __init__(self, proxies = None):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        self.headers = {'user-agent':self.user_agent}
        self.url_template = 'https://need.to.find/out'
        self.proxies = proxies
    
    def _url(self, i_code):
        url = self.url_template.format(str(i_code))
        return url
        
    def _headers(self, params = dict()):
        assert isinstance(params, dict)
        headers = self.headers.copy()
        headers.update(params)
        return headers
        
    def _proxies(self):
        proxies = self.proxies       
        return proxies
    
    def _request(self, i_code):
        url = self._url(i_code)
        headers = self._headers()
        proxies = self._proxies()
        response = requests.get(url, headers = headers, proxies = proxies, timeout = 10)
        return response

    def _parse(self, response):
        name = None
        price = None
        '''
        Need to be done
        '''
        return name, price
        
    def query(self, i_code):
        try:
            response = self._request(i_code)
            name, price = self._parse(response)
            return name, price
        except:
            return None, None
        

        
        