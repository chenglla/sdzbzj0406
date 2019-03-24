import scrapy
import json
from lulu.items import ScoreSchoolMajorItem
import pymysql


class ScoreSchoolMajor(scrapy.Spider):
    name = 'scoreSchoolMajorRight'
    headers = {
        'Host': 'gkcx.eol.cn',
        # 'Referer':'https://gkcx.eol.cn/school/54'
        'Referer': 'https://gkcx.eol.cn/school/557/specialtyline',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'lulu.pipelines.ScoreSchoolMajorPipeline': 301,
        }
    }

    def start_requests(self):
        start_urls = [
            'https://gkcx.eol.cn/api?uri=hxsjkqt/api/gk/score/special&year=2016&size=20&page=1',
            'https://gkcx.eol.cn/api?uri=hxsjkqt/api/gk/score/special&year=2015&size=20&page=1',
            'https://gkcx.eol.cn/api?uri=hxsjkqt/api/gk/score/special&year=2014&size=20&page=1',
            'https://gkcx.eol.cn/api?uri=hxsjkqt/api/gk/score/special&year=2017&size=20&page=1',
        ]
        for url in start_urls:
        # start_urls = ['https: // data - gkcx.eol.cn / soudaxue / queryschool.html?messtype = json & page = 1 & size = 2843']
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    # 解析首页
    def parse(self, response):
        print("response!!!!!!!!!!")
        # print(response)
        doc = json.loads(response.body_as_unicode())
        # print(len(doc))
        # if len(doc) != 1:
        datas = doc['data']['item']
        # print(len(datas))
            # a = json.loads(response.body_as_unicode())['totalRecord']



        for data in datas:
            if data['max'] == "--":
                data['max'] = 0
            if data['min'] == "--":
                data['min'] = 0
            score_school_major_items = ScoreSchoolMajorItem()

            score_school_major_items['schoolcode'] = data['name']
            score_school_major_items['year'] = data['year']
            score_school_major_items['type'] = "高考录取"

            score_school_major_items['category'] = data['local_type_name']
            score_school_major_items['majorcode'] = data['spname']
            score_school_major_items['batch'] = data['local_batch_name']
            score_school_major_items['highestscore'] = data['max']
            score_school_major_items['lowestscore'] = data['min']
            # print('最高分：',score_school_major_items['highestscore'])
            # print('最低分：',score_school_major_items['lowestscore'])
            yield score_school_major_items

        # 请求下一页的链接
        url = response.url
        # print(url)
        # 先以&分开，得到page变量，再用=分开得到page的值
        list = url.split('&')
        page = int(list[3].split('=')[1])
        # if page < 95:
        if page < 22330:
            page += 1
            newUrl = list[0] +'&'+list[1]+'&'+list[2]+ '&page=' + str(page)
            # print(newUrl)
            yield scrapy.Request(url=newUrl, callback=self.parse, headers=self.headers)