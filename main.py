import os
import sys
import time
import urllib2
import logging
import traceback
import sqlobject

import wp
import settings

url_queue = [] # list of tuples of url * callback * retries

try:
    conn = sqlobject.connectionForURI(settings.CONNECTION_STRING)
    sqlobject.sqlhub.processConnection = conn
except:
    logging.error("Database connection failed : %s", sys.exc_info())
    sys.exit(-1)

# Config logger, output to both file and console
logging.basicConfig(level=settings.LOG_LEVEL, filename=settings.LOG_FILE)
console = logging.StreamHandler()
console.setLevel(settings.LOG_LEVEL)
logging.getLogger('').addHandler(console)

def load_sites():
    """
    Each python file in sites/ directory except __init__.py and basesite.py contains
    a class that deals with a specific site. This class is exported via the 
    'export' variable.
    """
    return [
        __import__('sites.%s' % f.rstrip('.py'), globals(), locals(), ['export']).export
        for f in os.listdir('sites')
        if f.endswith('.py') and f != '__init__.py' and f != 'basesite.py']

while 1:       
    for site in load_sites():
        s = site(url_queue) 
        s.register_urls()
    
    # Fetch and process pages.
    while len(url_queue) > 0:
        url, callback, retries = url_queue.pop()
        try:
            p = urllib2.urlopen(url).read()
            callback(url, p)
        except urllib2.URLError:
            if retries > 0:
                logging.debug("%s failed, scheduled to try again", url)
                url_queue.insert(0, (url, callback, retries-1))
            else:
                logging.debug("%s failed", url)
        except AttributeError:
            logging.warning('%s no groupon today', url)
        except:
            logging.error("%s, stack trace:\n%s", sys.exc_info(), traceback.format_exc())
    
    logging.debug("Done.")
    wp.sync_categories()
    wp.sync_posts()
    time.sleep(settings.UPDATE_INTERVAL)
