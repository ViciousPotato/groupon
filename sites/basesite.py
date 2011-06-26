#coding: utf8
import re
import sys
import logging

import chardet
from BeautifulSoup import BeautifulSoup
from sqlobject.sqlbuilder import AND

sys.path.append('../')
import settings
import utils
from models import City, Site, Deal

# base class
class BaseSite(object):
    def __init__(self, url_queue):
        self.index_urls = {}
        self.url_queue = url_queue
        self.logger = logging.getLogger('sites.%s' % self.__class__.__name__)
        self.initialize()

    def register_urls(self):
        for url in self.index_urls.keys():
            self.url_queue.append((url, self._index_url_callback, settings.URL_RETRIES))
    
    def _index_url_callback(self, url, page):
        encoding = chardet.detect(page)['encoding']
        if encoding is not '':
            # Fix some Chinese sites with wrong encoding
            page = page.decode(encoding, 'ignore')
        self.index_url_callback(url, BeautifulSoup(page))
    
    def save_to_db(self, dic):
        assert all(map(dic.has_key, ['title', 'original_price', 'price', 'detail', 'url'])),\
            "Information incomplete."
        
        url = dic['url']
        original_price = dic['original_price'].text.encode('utf8')
        price = dic['price'].text.encode('utf8')
        title = dic['title'].text # title is unicode
        detail = dic['detail'].renderContents(encoding='utf8')
        detail = utils.clean_detail(detail, self.home_url)
            
        # Data formatting & validation.
        try:
            original_price, price = map(lambda s: int(re.search(r'(\d+)', s).group()),
                                        [original_price, price])
        except TypeError:
            logging.error("Price conversion failed. Detailed info: %s", [original_price, price])
            return
        except AttributeError:
            logging.error("Regex failed on %s", [original_price, price])
            return
        
        if len(title) > 500 or len(title) < 10:
            logging.error("Title length too short or too long : %s", title)
            return
        
        if len(detail) < 20:
            logging.error("Detail too short. %s", detail)
            return

        # Save to db.
        try:
            site = Site.select(Site.q.url == self.home_url)
            assert(site.count() == 1), "%s not found or dups." % self.home_url
            
            title = utils.lstrip(title, [s.decode('utf8') for s in ('今日团购', '今日精选', '：')])
            title = title.strip()
            title='[%s] %s' % (site[0].name, title)
            
            city_name = self.index_urls[url]
            city = City.select(City.q.name == city_name.decode('utf8'))
            assert city.count() == 1, "%s not found or dups." % city_name
            cityID = city[0].id
            
            if Deal.select(AND(Deal.q.title == title, Deal.q.cityID == cityID)).count() > 0:
                logging.info("Title dups %s" % title)
                return
            deal = Deal(url=url, title=title, price=price, originalPrice=original_price,
                        detail=detail.decode('utf8'),cityID=cityID, siteID=site[0].id)
            logging.info('%s OK', url)
        except:
            # Simple handling for the moment.
            logging.error("Error occured while saving data : %s", sys.exc_info())
