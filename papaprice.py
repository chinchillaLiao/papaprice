

import re
import requests

#爬爬價
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
        self.re_name = re.compile('(?<=\<h3\>)[^<>]*(?=\</h3\>)')
        self.re_price = re.compile('(?<=\<span\>)[0-9,]+(?=\</span\>)')
    
    def _parse(self, response):
        name = None
        price = None
        html = response.text
        name = self.re_name.search( html )[0]
        price = self.re_price.search( html )[0]
        price = int(price.replace(',',''))
        return name, price

        
class PP_pchome(PapaPrice):
    def __init__(self, proxies = None):
        super().__init__(proxies)
        self.url_template = 'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{}&fields=Seq,Id,Name,Price&_callback=jsonp_prod&1619356140?_callback=jsonp_prod'
        self.re_name = re.compile('(?<="Name":")[^"]+(?=")')
        self.re_price = re.compile('(?<="P":)\d+(?=,)')
    
    def _parse(self, response):
        name = None
        price = None
        html = response.text
        name = self.re_name.search( html )[0]
        price = self.re_price.search( html )[0]
        price = int(price)
        return name, price

        
class PP_etmall(PapaPrice):
    def __init__(self, proxies = None):
        super().__init__(proxies)
        self.url_template = 'https://www.etmall.com.tw/i/{}'
        self.re_name = re.compile("(?<='name': ')[^']+(?='\W+'price')")
        self.re_price = re.compile("(?<='price': ')[^']+(?=')")
        
    def _parse(self, response):
        name = None
        price = None
        html = response.text
        name = self.re_name.search( html )[0]
        price = self.re_price.search( html )[0]
        price = int(price)
        return name, price

        
class PP_yahoo(PapaPrice):
    def __init__(self, proxies = None):
        super().__init__(proxies)
        self.url_template = 'https://tw.buy.yahoo.com/gdsale/gdsale.asp?gdid={}'
        self.re_name = re.compile('(?<="name":")[^"]+(?="},{")')
        self.re_price = re.compile('(?<="TWD","price":")\d+')
        
    def _parse(self, response):
        name = None
        price = None
        html = response.text
        name = self.re_name.search( html )[0]
        price = self.re_price.search( html )[0]
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

        

        
        