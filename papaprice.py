#爬爬價
import time
import re
import requests
import sqlite3
from collections.abc import Iterable

# step 1.
# 建立資料庫，用來儲存商品資訊



# step 2.
# 建立簡單的寫入功能
class DB_Papaprice:
    def __init__(self, tbNames = [], dbName = 'papaprice.db'):
        self.dbName = dbName
    
        assert isinstance( tbNames, Iterable)
        
        for name in tbNames:
            assert isinstance (name, str)
            self._create_table(name)
            
        
    def _create_table(self, tbName):
        try:
            conn = sqlite3.connect(self.dbName)
            sql = f'''
                CREATE TABLE {tbName} (
                    i_code TEXT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    date TEXT DEFAULT CURRENT_TIMESTAMP
                );
            '''
            conn.execute(sql)
            conn.commit()
        except:
            pass
        finally:
            if conn:
                conn.close()   
                
    def record_price(self, i_code, name, price):
        sql = """
            INSERT OR REPLACE INTO momo (i_code, name, price) VALUES (?,?,?)
        """
        try:
            conn = sqlite3.connect(self.dbName)
            conn.execute(sql, (i_code, name, price,) )
            conn.commit()
            conn.close()
            return True
        except:
            if conn:
                conn.close()
            return False


# step.3
# 將要追蹤的商品的名稱&價格抓下來並寫入資料庫中

items = ['7490474', '8366451', 'awdfsdfs']  # 要追蹤的商品清單


class PapaPrice:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        self.headers = {'user-agent':self.user_agent}
        self.d_url = {
            #'momo':   'https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code={}', # 富邦MOMO
            #'pchome': 'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{}&fields=Seq,Id,Name,Price&_callback=jsonp_prod&1619356140?_callback=jsonp_prod',                           # 網路家庭PCHOME
            #'etmall': 'https://www.etmall.com.tw/i/{}',                              # 東森購物ETMALL
            #'yahoo':  'https://tw.buy.yahoo.com/gdsale/gdsale.asp?gdid={}',          # 雅虎購物Yahoo
            'shopee': 'https://shopee.tw/--i.{}',                                    # 蝦皮購物SHOPEE
        }
        
        self.db = DB_Papaprice(self.d_url.keys())
        
        self.d_items = {
            'momo':   ['7490474', '8366451'],
            'pchome': ['QCAM06-A90093QWP','DCAH86-A900ANO2C'],
            'etmall': ['2909324','2830187'],
            'yahoo':  ['9366406', '8192026'], 
            'shopee': ['6982233.3700005347', '13263679.5962852115'],
        
        }
        self.d_re_name = {
            'momo':   '(?<=\<h3\>)[^<>]*(?=\</h3\>)',
            'pchome': '(?<="Name":")[^"]+(?=")',
            'etmall': "(?<=GA_DIMENSION\.PRODUCT_NAME, ')[^']+(?=')",
            'yahoo':  '(?<=Product","name":")[^"]+(?=")', 
            'shopee': '(?<=\<div class="attM6y"\>\<span\>)[^<>]*(?=\</span\>\</div\>)',            
       
        }
        
        self.d_re_price = {
            'momo':   '(?<=\<span\>)[0-9,]+(?=\</span\>)',
            'pchome': '(?<="P":)\d+(?=,)', 
            'etmall': "(?<='price': )\d+",
            'yahoo':  '(?<="price":")\d+(?=")', 
            'shopee': '(?<=\<div class="_3e_UQT"\>\$)[0-9,]+(?=\</div\>)',            
        
        }


      
        
    def update(self):
        for ec, url_template in self.d_url.items():
            items = self.d_items[ec]
            re_name = self.d_re_name[ec]
            re_price = self.d_re_price[ec]
            
            rec_name = re.compile(re_name)
            rec_price = re.compile(re_price)
            
            for i_code in items:
                url = url_template.format(i_code)
                print(url)
                SUCCESS = False
                name = 'unknown'
                price = None
                try:
                    resp = requests.get(url, headers = self.headers, timeout = 10)
                    print(resp)
                    html = resp.text
                    #print(html)
                    name = rec_name.search( html )[0]
                    print(name)
                    price = rec_price.search( html )[0]
                    print(price)
                    SUCCESS = self.db.record_price(i_code, name, price)
                    
                except Exception as e:
                    print(e)
                    
                finally:
                    print(SUCCESS, i_code, price, name)
                    
                time.sleep(3)
        

        
        