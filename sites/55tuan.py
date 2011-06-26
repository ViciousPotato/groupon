#coding: utf8
import basesite

class Site55(basesite.BaseSite):
    def initialize(self):
        self.home_url = 'http://www.55tuan.com'
        self.index_urls = {'http://www.55tuan.com' : '北京'}

    def index_url_callback(self, url, soup):
        title = soup.find('div', {'class' : 'biaoti'})
        price = soup.find('div', {'class' : 'buy'}).ul.li
        original_price = soup.find('div', {'class' : 'buy_bottom'}).findAll('span')[1]
        detail = soup.find('div', {'class' : 'benci'})
        self.save_to_db(locals())

export = Site55
