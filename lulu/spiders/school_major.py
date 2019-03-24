import scrapy
import json
from lulu.items import DynamicItem
import pymysql

class SchoolMajor(scrapy.Spider):
    name = 'schoolMajor'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Referer': 'https://gkcx.eol.cn/soudaxue/queryschool.html',
        'Content-Type': 'application/json',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'lulu.pipelines.DynamicPipeline': 301,
        }
    }

    def start_requests(self):
        start_urls = [
            'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&page=1&size=2844',]
        # start_urls = ['https: // data - gkcx.eol.cn / soudaxue / queryschool.html?messtype = json & page = 1 & size = 2843']
        yield scrapy.Request(url=start_urls[0], callback=self.parse, headers=self.headers)


    def parse(self, response):
        print("response!!!!!!!!!!")
        # print(response)
        doc = json.loads(response.body_as_unicode())
        # print(len(doc))
        if len(doc) != 1:
            datas = doc['school']
        # a = json.loads(response.body_as_unicode())['totalRecord']
        # print(a)
        # print(datas)

            for data in datas:
                # item = DynamicItem()
                majorcode = 'https://gkcx.eol.cn/schoolhtm/schoolTemple/school' + str(data['schoolid']) + '.htm'
                # item['schoolcode'] = data['schoolcode']
                # item['degreetype'] =data['level']
                # item['majorcode'] = majorcode
                # item['href'] = data['guanwang']
                # item['schoolname'] = data['schoolname']

                yield scrapy.Request(url=majorcode, meta={'data': data}, callback=self.parse_major_href)
                # request.meta['data'] = data

                # item['major'] = scrapy.Request(url=item['majorcode'], callback=self.parse_major_href, headers=self.headers)


                # print(data['schoolcode'])
                # yield item

        #请求下一页的链接
        url = response.url
        # print(url)
        #先以&分开，得到page变量，再用=分开得到page的值
        list = url.split('&')
        page = int(list[1].split('=')[1])
        # if page < 95:
        if page < 95:
            page+=1
            newUrl = list[0] + '&page=' + str(page) + '&'+list[2]
            # print(newUrl)
            yield scrapy.Request(url=newUrl, callback=self.parse, headers=self.headers)
            # # # 存入数据库
            # connection = pymysql.connect(host="47.93.225.12", port=3306, user="zkrt", passwd="zkrtFCZ812",
            #                              db="school-matriculate",
            #                              charset='utf8')
            # cursor = connection.cursor()
            #
            # sql = "insert into `school_major` (`schoolcode`,`majorcode`,`degreetype`) values " \
            #       "('%s','%s','%s')" \
            #       % (
            #           item["schoolcode"], item["majorcode"], item["degreetype"])
            #
            # # sql = "insert into `province_info` (`provincename`,`provincecode`,`description`,`inserttime`,`updatetime`) values " \
            # #       "('%s','%s','%s','%s','%s')" \
            # #       % (
            # #           lulu['provincename'], lulu['provincecode'], lulu['description'], lulu['inserttime'],
            # #           lulu['updatetime'])
            # cursor.execute(sql)
            # connection.commit()
    def parse_major_href(self,response):
        data = response.meta['data']
        list = response.css('body > div.main.center > div > ul > div:nth-child(3) > div > ul > li:nth-child(3) ')
        majorHref = list.css('a::attr(href)').extract_first().lstrip()
        majorText = list.css('a::text').extract_first()
        print(majorHref, majorText)
        majorUrl = 'https://gkcx.eol.cn'+majorHref
        print(majorUrl)
        yield scrapy.Request(url=majorUrl, meta={'data': data}, callback=self.parse_major)
        # request2.meta['data'] = data
        # yield scrapy.Request(url=majorHref, callback=self.parse_major(), headers=self.headers)


    def parse_major(self,response,):
        data = response.meta['data']
        majors = response.css('body > div.main.center > div > div.left.w-670 > div.content.news > ul > li > a::text').extract()
        print(majors)
        for major in majors:
            item = DynamicItem()
            item['schoolcode'] = data['schoolcode']
            item['degreetype'] = data['level']
            # item['majorcode'] = 'https://gkcx.eol.cn/schoolhtm/schoolTemple/school' + str(data['schoolid']) + '.htm'
            # item['href'] = data['guanwang']
            item['schoolname'] = data['schoolname']
            item['majorname'] = major
            yield item
            # # 存入数据库
            connection = pymysql.connect(host="47.93.225.12", port=3306, user="zkrt", passwd="zkrtFCZ812",
                                         db="school-matriculate",
                                         charset='utf8')
            cursor = connection.cursor()

            sql = "insert into `school_majorname` (`schoolcode`,`schoolname`,`majorname`,`degreetype`) values " \
                  "('%s','%s','%s','%s')" \
                  % (
                      item['schoolcode'], item['schoolname'], item['majorname'],item['degreetype'])

            # sql = "insert into `province_info` (`provincename`,`provincecode`,`description`,`inserttime`,`updatetime`) values " \
            #       "('%s','%s','%s','%s','%s')" \
            #       % (
            #           lulu['provincename'], lulu['provincecode'], lulu['description'], lulu['inserttime'],
            #           lulu['updatetime'])
            cursor.execute(sql)
            connection.commit()
