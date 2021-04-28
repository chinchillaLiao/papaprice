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
        response = self._request(i_code)
        name, price = self._parse(response)
        return name, price
 
 
class PP_momo(PapaPrice):
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

        
class PP_pchome(PapaPrice):
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

        
class PP_etmall(PapaPrice):
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

        
class PP_yahoo(PapaPrice):
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
        
        
class PP_shopee(PapaPrice):
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
        price = price/1000
        return name, price

        

        
        