#coding: utf8
import basesite

class SiteAifu(basesite.BaseSite):
    def initialize(self):
        self.home_url = 'http://www.ftuan.com'
        self.index_urls = {'http://www.ftuan.com/city.php?ename=bjcy' : '北京',
                           'http://www.ftuan.com/city.php?ename=bjhd' : '北京'}
    
    def index_url_callback(self, url, soup):
        # Same with meituan.
        deal = soup.find('div', id='deal-intro')
        title = deal.h1
        price = deal.find('p', {'class' : 'deal-price'})
        original_price = deal.table.findAll('td')[0]
        detail = soup.find('div', id='deal-stuff')
        self.save_to_db(locals())

export = SiteAifu
