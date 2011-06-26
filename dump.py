import webbrowser

import sqlobject

import settings
from models import Deal

conn = sqlobject.connectionForURI(settings.CONNECTION_STRING)
sqlobject.sqlhub.processConnection = conn

deals = Deal.select()
f = open('dump.html', 'wb')

print >> f, """
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
</head>
<body>
"""
for deal in deals:
    print >> f, '<li>'
    print >> f, '<ul>'
    print >> f, '<li>%s</li>' % deal.title.encode('utf8')
    print >> f, '<li>%s/%s</li>' % (deal.price, deal.originalPrice)
    print >> f, '<li>%s</li>' % deal.detail.encode('utf8')
    print >> f, '</ul>'
    print >> f, '</li>'
print >> f, '</ul>'
print >> f, '</body>'
print >> f, '</html>'

f.close()

webbrowser.open('dump.html')
