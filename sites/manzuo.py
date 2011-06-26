#coding: utf8
import basesite

class SiteManzuo(basesite.BaseSite):
    def initialize(self):
        self.home_url = 'http://www.manzuo.com'
        self.index_urls = {'http://www.manzuo.com/beijing/index.htm'  : '北京',
                           'http://www.manzuo.com/shanghai/index.htm' : '上海',
                           'http://www.manzuo.com/qingdao/index.htm'  : '青岛'}
        
    def index_url_callback(self, url, soup):
        deal = soup.find('div', {'class' : 'con_02'})
        title = deal.h2
        original_price = deal.table.findAll('td')[0]
        price = deal.find('div', {'class' : 'new_con_buy_01'})
        detail = soup.find('div', {'class' : 'con_15'})
        self.save_to_db(locals())

export = SiteManzuo
