#coding: utf8
import basesite

class SiteMeituan(basesite.BaseSite):
    def initialize(self):
        self.home_url = 'http://www.meituan.com'
        self.index_urls = {'http://www.meituan.com/beijing' : '北京',
                           'http://www.meituan.com/shanghai': '上海',
                           'http://www.meituan.com/wuhan'   : '武汉'}

    def index_url_callback(self, url, soup):
        deal = soup.find('div', id='deal-intro')
        title = deal.h1
        price = deal.find('p', {'class' : 'deal-price'})
        original_price = deal.table.findAll('td')[0]
        detail = soup.find('div', id='deal-stuff')
        self.save_to_db(locals())
    
export = SiteMeituan
