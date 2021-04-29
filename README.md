# papaprice 爬爬價
爬MOMO、PCHOME、ETMALL、SHOPEE、YAHOO 商品名稱與價格

```python
from papaprice import Etmall, Momo, Pchome, Shopee, Yahoo

# https://www.etmall.com.tw/i/2886010
etmall = Etmall()
print('etmall', etmall.query('2886010'))
# etmall ('Apple iPhone 12 Pro 128G 智慧型 5G 手機', 32388)

# https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8169274
momo = Momo()
print('momo', momo.query('8169274'))
# momo ('【Apple 蘋果】iPhone 12 Pro 128G 6.1吋(超值殼貼組)', 33000)

# https://24h.pchome.com.tw/prod/DYAJIM-A900B724R
pchome = Pchome()
print('pchome', pchome.query('DYAJIM-A900B724R'))
# pchome ('Apple iPhone 12 Pro (128G)-太平洋藍(MGMN3TA/A)', 32900)

# https://shopee.tw/--i.54598032.5857088290
shopee = Shopee()
print('shopee', shopee.query('54598032.5857088290'))
# shopee ('APPLE iPhone 12 Pro 128G 支援5G上網/A14 CPU 送門市現場保貼服務兌換券', 32940)

# https://tw.buy.yahoo.com/gdsale/-9205108.html
yahoo = Yahoo()
print('yahoo', yahoo.query('9205108'))
# yahoo ('Apple iPhone 12 PRO 128G 6.1吋智慧型手機', 32600)
```

# 支援 proxies 使用，避免大量查詢被封鎖。
```python
proxies = {
    'https':'https://your.proxy.link',
    'http':'http://your.proxy.link',
}

# https://www.etmall.com.tw/i/2886010
etmall = Etmall(proxies)
print('etmall', etmall.query('2886010'))
# etmall ('Apple iPhone 12 Pro 128G 智慧型 5G 手機', 32388)
```

# proxies 設定，以服務供應商 [Bright Data](https://brightdata.grsm.io/twforthewin) 為例 ->[連結](https://brightdata.grsm.io/twforthewin)
```python
clientname = '你在Bright Data的用戶名' #注意：每種不同的Proxy服務，有不同的用戶名。
password = '對應的密碼'
proxy = f'https://{username}:{pwssword}@zproxy.lum-superproxy.io:22225'
proxies = {'https':proxy}

# https://www.etmall.com.tw/i/2886010
etmall = Etmall(proxies)
print('etmall', etmall.query('2886010'))
# etmall ('Apple iPhone 12 Pro 128G 智慧型 5G 手機', 32388)
```
