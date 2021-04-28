# papaprice
爬MOMO、PCHOME、ETMALL、SHOPEE、YAHOO 商品名稱與價格

```python
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
