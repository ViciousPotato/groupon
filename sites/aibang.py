#coding: utf8
import basesite

class SiteAibang(basesite.BaseSite):
    def initialize(self):
        self.home_url = 'http://tuan.aibang.com'
        self.index_urls = {'http://tuan.aibang.com/tuancity' : '北京'}
        
    def index_url_callback(self, url, soup):
        title = soup.find('table', {'class' : 'at_jrat'}).findAll('td')[-1]
        original_price = soup.find('div', {'class' : 't_deal_l'}).strong
        price = soup.find('div', {'class' : 'at_buy'})
        detail = soup.find('div', {'class' : 't_detail_l'})
        self.save_to_db(locals())

export = SiteAibang
