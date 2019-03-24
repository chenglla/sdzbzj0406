import scrapy
import json
from lulu.items import SchoolInfoItem


class SchoolInfo(scrapy.Spider):
    name = 'schoolInfo'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        # 'Referer': 'https://gkcx.eol.cn/soudaxue/queryschool.html?&province=%E5%8C%97%E4%BA%AC',
        # 'Referer': 'https://gkcx.eol.cn/soudaxue/queryschool.html',
        'Referer': 'https://gkcx.eol.cn/soudaxue/queryschool.html?&province=%E5%A4%A9%E6%B4%A5',
        'Content-Type': 'application/json',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'lulu.pipelines.SchoolInfoPipeline': 301,
        },
    }

    def start_requests(self):
        start_urls = [
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&page=1&size=2844',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%8C%97%E4%BA%AC&page=1&size=50',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%A4%A9%E6%B4%A5&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%B2%B3%E5%8C%97&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%B2%B3%E5%8D%97&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%B1%B1%E4%B8%9C&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%B1%B1%E8%A5%BF&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E9%99%95%E8%A5%BF&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%86%85%E8%92%99%E5%8F%A4&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E8%BE%BD%E5%AE%81&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%90%89%E6%9E%97&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E9%BB%91%E9%BE%99%E6%B1%9F&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E4%B8%8A%E6%B5%B7&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%B1%9F%E8%8B%8F&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%AE%89%E5%BE%BD&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%B1%9F%E8%A5%BF&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%B9%96%E5%8C%97&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%B9%96%E5%8D%97&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E9%87%8D%E5%BA%86&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%9B%9B%E5%B7%9D&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E8%B4%B5%E5%B7%9E&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E4%BA%91%E5%8D%97&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%B9%BF%E4%B8%9C&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%B9%BF%E8%A5%BF&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E7%A6%8F%E5%BB%BA&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E7%94%98%E8%82%83&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E5%AE%81%E5%A4%8F&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%96%B0%E7%96%86&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E8%A5%BF%E8%97%8F&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%B5%B7%E5%8D%97&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%B5%99%E6%B1%9F&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E9%9D%92%E6%B5%B7&page=1&size=30',
            # 'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E9%A6%99%E6%B8%AF&page=1&size=30',
            'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=json&province=%E6%BE%B3%E9%97%A8&page=1&size=30',
        ]
        yield scrapy.Request(url=start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self,response):
        doc = json.loads(response.body_as_unicode())
        # print(len(doc))
        if len(doc) != 1:
            datas = doc['school']

            for data in datas:
                #获取通讯电话和地址
                schoolInfo_items = SchoolInfoItem()
                schoolInfo_items['school_name_cn']=""
                schoolInfo_items['school_name_en'] =""
                schoolInfo_items['schoolcode'] =""
                schoolInfo_items['abbreviation']=""
                schoolInfo_items['province']=""
                schoolInfo_items['city']=""
                schoolInfo_items['grade']=""
                schoolInfo_items['buildtime']=""
                #
                schoolInfo_items['category']=""
                schoolInfo_items['type']=""
                schoolInfo_items['ascription']=""
                schoolInfo_items['address']=""
                schoolInfo_items['tel']=""
                schoolInfo_items['summary']=""
                schoolInfo_items['website']=""
                schoolInfo_items['alumni']=""
                #
                schoolInfo_items['motto']=""
                schoolInfo_items['logo']=""
                schoolInfo_items['picture']=""
                schoolInfo_items['keydiscipline']=""
                schoolInfo_items['ranking']=""
                phone_address = 'https://gkcx.eol.cn/schoolhtm/schoolTemple/school' + str(data['schoolid']) + '.htm'
                keydiscipline = 'https://gkcx.eol.cn/schoolhtm/schoolInfo/' +  str(data['schoolid']) + '/10137/detail.htm'
                picture = 'https://gkcx.eol.cn/schoolhtm/' +  str(data['schoolid']) + '/schoolImageList/list_1.htm'
                yield scrapy.Request(url=phone_address, callback=self.phone_address_parse, headers=self.headers, meta={'data': data, 'schoolInfo_items': schoolInfo_items})
                yield scrapy.Request(url=keydiscipline, callback=self.keydiscipline_parse, headers=self.headers, meta={'data': data, 'schoolInfo_items': schoolInfo_items})
                yield scrapy.Request(url=picture, callback=self.picture_parse, headers=self.headers, meta={'data': data, 'schoolInfo_items': schoolInfo_items})


        # TODO 请求下一页的连接
        # url = response.url
        # print('当前页：',url)
        # # 先以&分开，得到page变量，再用=分开得到page的值
        # list = url.split('&')
        # page = int(list[2].split('=')[1])
        # # if page < 95:
        # if page < 4:
        #     page += 1
        #     newUrl = list[0]+ '&'+list[1] + '&page=' + str(page) + '&' + list[3]
        #     print('下一页：',newUrl)
        #     yield scrapy.Request(url=newUrl, callback=self.parse, headers=self.headers)

    def phone_address_parse(self, response):
        data = response.meta['data']
        schoolInfo_items = response.meta['schoolInfo_items']

        #获取通讯地址
        address = response.css('body > div.main.center > div > div.li-collegeHome > div.li-collegeUl > ul.li-collegeInfo.li-ellipsis > li:nth-child(2) > div > span::text').extract_first()
        # if len(address) != 0:
        #     schoolInfo_items['address'] = address
        # else:
        #     schoolInfo_items['address'] = ""
        #     address = ""
        # print('地址：', address)
        phone = response.css('body > div.main.center > div > div.li-collegeHome > div.li-collegeUl > ul:nth-child(3) > li:nth-child(4) > div > span::text').extract_first()
        # if len(phone) != 0:
        #     schoolInfo_items['tel'] = phone
        # else:
        #     schoolInfo_items['tel'] = ""
            # phone = ""
        # print('电话：',phone)
        #学校logo
        logo = response.css(
            'body > div.main.center > div > div.li-collegeHome > div.left.li-collegeLogo > img::attr(src)').extract_first()
        # schoolInfo_items = SchoolInfoItem()

        schoolInfo_items['school_name_cn'] = data['schoolname']
        schoolInfo_items['school_name_en'] = ""
        schoolInfo_items['schoolcode'] = data['schoolcode']
        schoolInfo_items['abbreviation'] = data['oldname']
        schoolInfo_items['province'] = data['province']

        schoolInfo_items['city'] = data['province']

        #等级
        if data['f985'] == "1":
            grade = "985"
        elif data['f211'] == "1":
            grade = "211"
        else:
            grade = data['level']
        schoolInfo_items['grade'] = grade
        schoolInfo_items['buildtime'] = ""   #建校时间
        schoolInfo_items['category'] = data['schoolnature']  #公立大学、民办大学等，  以英文分号;作为分割符号
        schoolInfo_items['type'] = data['schoolproperty']  #理工类、综合类、文史类等

        schoolInfo_items['ascription'] = data['membership']   #归属属性，如中央部署高校
        schoolInfo_items['address'] = address
        schoolInfo_items['tel'] = phone
        schoolInfo_items['summary'] = data['jianjie']
        schoolInfo_items['website'] = data['guanwang']
        schoolInfo_items['alumni'] = ""  #知名校友

        schoolInfo_items['motto'] = ""  #校训
        schoolInfo_items['logo'] = logo
        # schoolInfo_items['picture'] = data['']   #学校实景图片，最多三张， 以英文分号;作为分割符号
        # schoolInfo_items['keydiscipline'] = data['']   #重点学科
        schoolInfo_items['ranking'] = data['ranking']  #综合排名

        # return schoolInfo_items
        yield schoolInfo_items
    def keydiscipline_parse(self,response):
        data = response.meta['data']
        schoolInfo_items = response.meta['schoolInfo_items']
        # print(response.text)

        keydisciplineList = response.css(
            'body > div.main.center > div > div.left.w-670 > div.content.news > table > tbody > tr > td:nth-child(2)::text').extract_first()
        keydisciplineList1 = response.css(
            'body > div.main.center > div > div.left.w-670 > div.content.news > p:nth-child(2) > span::text').extract_first()
        keydisciplineList2 = response.css('body > div.main.center > div > div.left.w-670 > div.content.news > p:nth-child(2)::text').extract_first()
        keydisciplineList3 = response.css('body > div.main.center > div > div.left.w-670 > div.content.news > div::text').extract_first()
        if keydisciplineList is not None:
            schoolInfo_items['keydiscipline'] = keydisciplineList  # 重点学科


        elif keydisciplineList1 is not None:
            schoolInfo_items['keydiscipline'] = keydisciplineList1  # 重点学科
        elif keydisciplineList2 is not None:
            schoolInfo_items['keydiscipline'] = keydisciplineList2  # 重点学科
        elif keydisciplineList3 is not None:
            schoolInfo_items['keydiscipline'] = keydisciplineList3  # 重点学科
        else:
            schoolInfo_items['keydiscipline'] = ""
        # print(schoolInfo_items['keydiscipline'])
        # return schoolInfo_items
        yield schoolInfo_items
    def picture_parse(self,response):
        data = response.meta['data']
        schoolInfo_items = response.meta['schoolInfo_items']

        url1 = response.css('#image_xixi-4 > a > img::attr(src)').extract_first()
        url2 = response.css('#image_xixi-2 > a > img::attr(src)').extract_first()
        url3 = response.css('#image_xixi-3 > a > img::attr(src)').extract_first()

        # print('url:',url1,url2,url3)
        picture_url = response.urljoin(url1)
        picture_url1 = response.urljoin(url2)
        picture_url2 = response.urljoin(url3)
        # print('picture_url:',picture_url,picture_url1,picture_url2)
        schoolInfo_items['picture'] = picture_url + ';' +picture_url1 + ';'+picture_url2
        # print('picture:',schoolInfo_items['picture'])
        # print(schoolInfo_items)
        yield schoolInfo_items