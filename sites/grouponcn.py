#coding: utf8
import basesite

class SiteTuanbao(basesite.BaseSite):
    def initialize(self):
        self.home_url = 'http://www.groupon.cn'
        self.index_urls = {'http://www.groupon.cn/checkcity/?cityid=10024' : '安庆',
                           'http://www.groupon.cn/checkcity/?cityid=1'     : '北京',
                           'http://www.groupon.cn/checkcity/?cityid=2'     : '长春',
                           'http://www.groupon.cn/checkcity/?cityid=3'     : '长沙',
                           'http://www.groupon.cn/checkcity/?cityid=10009' : '常州',
                           'http://www.groupon.cn/checkcity/?cityid=4'     : '成都',
                           'http://www.groupon.cn/checkcity/?cityid=5'     : '重庆',
                           'http://www.groupon.cn/checkcity/?cityid=6'     : '大连',
                           'http://www.groupon.cn/checkcity/?cityid=10035' : '东莞',
                           'http://www.groupon.cn/checkcity/?cityid=10005' : '东营',
                           'http://www.groupon.cn/checkcity/?cityid=10034' : '鄂州',
                           'http://www.groupon.cn/checkcity/?cityid=7'     : '福州',
                           'http://www.groupon.cn/checkcity/?cityid=8'     : '广州',
                           'http://www.groupon.cn/checkcity/?cityid=9'     : '贵阳',
                           'http://www.groupon.cn/checkcity/?cityid=10'    : '哈尔滨',
                           'http://www.groupon.cn/checkcity/?cityid=11'    : '杭州',
                           'http://www.groupon.cn/checkcity/?cityid=12'    : '合肥',
                           'http://www.groupon.cn/checkcity/?cityid=10016' : '衡阳',
                           'http://www.groupon.cn/checkcity/?cityid=10032' : '惠州',
                           'http://www.groupon.cn/checkcity/?cityid=14'    : '济南',
                           'http://www.groupon.cn/checkcity/?cityid=10010' : '济宁',
                           'http://www.groupon.cn/checkcity/?cityid=10012' : '金华',
                           'http://www.groupon.cn/checkcity/?cityid=15'    : '昆明',
                           'http://www.groupon.cn/checkcity/?cityid=16'    : '兰州',
                           'http://www.groupon.cn/checkcity/?cityid=10014' : '连云港',
                           'http://www.groupon.cn/checkcity/?cityid=10007' : '临沂',
                           'http://www.groupon.cn/checkcity/?cityid=18'    : '南昌',
                           'http://www.groupon.cn/checkcity/?cityid=19'    : '南京',
                           'http://www.groupon.cn/checkcity/?cityid=20'    : '南宁',
                           'http://www.groupon.cn/checkcity/?cityid=10022' : '南通',
                           'http://www.groupon.cn/checkcity/?cityid=10017' : '宁波',
                           'http://www.groupon.cn/checkcity/?cityid=21'    : '青岛',
                           'http://www.groupon.cn/checkcity/?cityid=22'    : '上海',
                           'http://www.groupon.cn/checkcity/?cityid=10029' : '邵阳',
                           'http://www.groupon.cn/checkcity/?cityid=10023' : '绍兴',
                           'http://www.groupon.cn/checkcity/?cityid=23'    : '深圳',
                           'http://www.groupon.cn/checkcity/?cityid=24'    : '沈阳',
                           'http://www.groupon.cn/checkcity/?cityid=25'    : '石家庄',
                           'http://www.groupon.cn/checkcity/?cityid=1243'  : '苏州',
                           'http://www.groupon.cn/checkcity/?cityid=26'    : '太原',
                           'http://www.groupon.cn/checkcity/?cityid=27'    : '天津',
                           'http://www.groupon.cn/checkcity/?cityid=10003' : '威海',
                           'http://www.groupon.cn/checkcity/?cityid=10004' : '潍坊',
                           'http://www.groupon.cn/checkcity/?cityid=10025' : '温州',
                           'http://www.groupon.cn/checkcity/?cityid=10008' : '无锡',
                           'http://www.groupon.cn/checkcity/?cityid=10018' : '芜湖',
                           'http://www.groupon.cn/checkcity/?cityid=1245'  : '武汉',
                           'http://www.groupon.cn/checkcity/?cityid=28'    : '西安',
                           'http://www.groupon.cn/checkcity/?cityid=29'    : '厦门',
                           'http://www.groupon.cn/checkcity/?cityid=10020' : '湘潭',
                           'http://www.groupon.cn/checkcity/?cityid=10027' : '襄樊',
                           'http://www.groupon.cn/checkcity/?cityid=10013' : '徐州',
                           'http://www.groupon.cn/checkcity/?cityid=10001' : '烟台',
                           'http://www.groupon.cn/checkcity/?cityid=10015' : '盐城',
                           'http://www.groupon.cn/checkcity/?cityid=10019' : '扬州',
                           'http://www.groupon.cn/checkcity/?cityid=10026' : '宜昌',
                           'http://www.groupon.cn/checkcity/?cityid=10021' : '镇江',
                           'http://www.groupon.cn/checkcity/?cityid=30'    : '郑州',
                           'http://www.groupon.cn/checkcity/?cityid=10031' : '中山',
                           'http://www.groupon.cn/checkcity/?cityid=10033' : '珠海',
                           'http://www.groupon.cn/checkcity/?cityid=10002' : '淄博'
                           }

    def index_url_callback(self, url, soup):
        prices = soup.find('div', {'class' : 'value'}).findAll('dl', limit=3)
        title = soup.find('div', {'class' : 'deal clearfix'}).div
        price = soup.find('div', {'class' : 'amount'}).b
        original_price = prices[0].dd
        detail = soup.find('div', {'class' : 'page_content clearfix'})
        self.save_to_db(locals())

export = SiteTuanbao
