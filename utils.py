import re
import sys
import urlparse

from HTMLParser import HTMLParser
from htmlentitydefs import entitydefs

# FIXME: Ugly implementation
class DetailCleaner(HTMLParser):
    result = ''
    ignore = False
    ignore_tags = ('script', 'style')
    
    def __init__(self, base_url=''):
        self.base_url = base_url
        HTMLParser.__init__(self)

    def handle_data(self, data):
        if not self.ignore:
            self.result += data.strip()
    
    def handle_charref(self, ref):
        self.result += "&#%(ref)s;" % locals()
        
    def handle_entityref(self, ref):
        if ref == 'nbsp':
            self.result += ' '
        else:
            self.result += '&%(ref)s' % locals()
            if entitydefs.has_key(ref):
                self.result += ';'
    
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            strattrs = ''
            for k,v in attrs:
                if k == 'src' and not v.startswith('http://'):
                    v = urlparse.urljoin(self.base_url, v)
                strattrs += ' %s="%s"' % (k, v)
            if isinstance(strattrs, unicode):
                strattrs = strattrs.encode('utf8')
            self.result += '<%(tag)s%(strattrs)s /> <br />' % locals()
        elif tag in self.ignore_tags:
            self.ignore = True

    def handle_endtag(self, tag):
        if tag == 'p':
            self.result += '<br />'
        elif tag.startswith('h'):
            self.result += '<br />'
        elif tag in self.ignore_tags:
            self.ignore = False

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.result += '<br />'
        elif tag == 'img':
            strattrs = ''
            for k,v in attrs:
                if k == 'src' and not v.startswith('http://'):
                    v = urlparse.urljoin(self.base_url, v)
                strattrs += ' %s="%s"' % (k, v)
            if isinstance(strattrs, unicode):
                strattrs = strattrs.encode('utf8')
            self.result += '<%(tag)s%(strattrs)s /> <br />' % locals()

    def output(self):
        return self.result

def clean_detail(detail, base_url):
    cleaner = DetailCleaner(base_url)
    cleaner.feed(detail)
    return cleaner.output()

def rstrip(string, strips):
    for strip in strips:
        string = re.sub(r'%s$' % strip, '', string)
    return string

def lstrip(string, strips):
    for strip in strips:
        string = re.sub(r'^%s' % strip, '', string)
    return string

if __name__ == '__main__':
    cleaner =  DetailCleaner()
    cleaner.feed(file(sys.argv[1]).read())
    print cleaner.output()

            
