#coding: utf8
import os
from datetime import datetime
import pickle

import lib.pyblog as pyblog

import sqlobject
import settings
import utils
import models

blog = pyblog.WordPress(settings.WP_URL, settings.WP_USERNAME, settings.WP_PASSWORD) 
conn = sqlobject.connectionForURI(settings.CONNECTION_STRING)
sqlobject.sqlhub.processConnection = conn

def sync_posts():
    #TODO: Handle exceptions   
    global blog
    if os.path.exists('storage'):
        s = open('storage')
        storage = pickle.load(s)
        s.close()
    else:
        storage = {'lastSyncTime' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')}    
    
    for deal in models.Deal.select(models.Deal.q.time >= storage['lastSyncTime']):
        city = models.City.select(models.City .q.id == deal.cityID)
        assert city.count() == 1
        price, original_price = map(lambda i: str(i).endswith('.0') and str(i)[:-2] or str(i),
                                    [deal.price, deal.originalPrice])
        custom_fields = [{'key' : 'price', 'value' : price},
                         {'key' : 'original_price', 'value' : original_price},
                         {'key' : 'url', 'value' : deal.url}]
        blog.new_post({'title' : deal.title, 'description' : deal.detail, 'categories' : [city[0].name],
                       'custom_fields' : custom_fields})
        print "Deal %s posted" % deal.id
    
    storage['lastSyncTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    s = open('storage', 'w')
    pickle.dump(storage, s)
    s.close()
    
    print "Post Sync Done"

def sync_categories():
    global blog
    categories = blog.get_categories()
    cities = [city.name for city in models.City.select()] 
    for category in categories:
        if category['categoryName'] in cities:
            cities.remove(category['categoryName'])
        elif category['categoryName'] not in ('Uncategorized', '未分类'.decode('utf8')):
            blog.delete_category(category['categoryId'])
            print "Category %s deleted." % category['categoryName']
    for city in cities:
        blog.new_category({'name' : city})
        print "Created category %s" % city
    print "Category Sync Done"

if __name__ == '__main__':
    sync_categories()
    sync_posts()