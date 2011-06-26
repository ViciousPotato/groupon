from sqlobject import *

# Unluckily, we can't use fromDatabase = True to generate class
# automatically, because that would trigger a hideous unicode bug.

class City(SQLObject):
    name = UnicodeCol()
    deals = MultipleJoin('Deal')
    class sqlmeta:
        table = 'cities'

class Site(SQLObject):
    name = UnicodeCol()
    url = StringCol()
    deals = MultipleJoin('Deal')
    class sqlmeta:
        table = 'sites'


class Deal(SQLObject):
    url = StringCol()
    title = UnicodeCol()
    detail = UnicodeCol()
    price = FloatCol()
    originalPrice = FloatCol()
    time = TimestampCol()
    city = ForeignKey('City')
    site = ForeignKey('Site')
    
    class sqlmeta:
        table = 'deals'

