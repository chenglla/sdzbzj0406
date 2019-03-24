# -*- coding: utf-8 -*-
import logging

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import json
import pymysql
from scrapy.crawler import Settings as settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LuluPipeline(object):
    def __init__(self):
        dbargs = dict(
            host = '47.93.225.12',
            db = 'school-matriculate',
            user = 'zkrt',  # replace with you user name
            passwd = 'zkrtFCZ812',  # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item
    def insert_into_table(self,conn,item):
        conn.execute(
                'insert into province_info(provincename,provincecode,description) values (%s,%s,%s)',
                (item['provincename'], item['provincecode'], item['description']))


class DynamicPipeline(object):
    def __init__(self):
        # 初始化一个文件
        self.file_name = open("CSDN首页文章信息.json", "wb")

    def process_item(self, item, spider):
        # 这里是将item先转换成字典，在又字典转换成字符串
        # json.dumps转换时对中文默认使用的ascii编码.想输出真正的中文需要指定 ensure_ascii=False
        # 将最后的item 写入到文件中
        text = json.dumps(dict(item), ensure_ascii=False) + "\n"
        text = text.encode()
        self.file_name.write(text)
        return item

    def close_spider(self,spider):
        self.file_name.close()
# class DynamicPipeline(object):
#     def __init__(self):
#         dbargs = dict(
#             host = '47.93.225.12',
#             db = 'school-matriculate',
#             user = 'zkrt',  # replace with you user name
#             passwd = 'zkrtFCZ812',  # replace with you password
#             charset = 'utf8',
#             cursorclass = MySQLdb.cursors.DictCursor,
#             use_unicode = True,
#         )
#         self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
#
#     def process_item(self, item, spider):
#         res = self.dbpool.runInteraction(self.insert_into_table, item)
#         return item
#     def insert_into_table(self,conn,item):
#         print("2222222222222222")
#             # conn.execute('insert into province_info(provincename,provincecode,description,inserttime,updatetime) values (%s,%s,%s,%s,%s)',
#             #              (item['provincename'],item['provincecode'],item['description'],item['inserttime'],item['updatetime']))
#
#         conn.execute(
#                 'insert into school_major(schoolcode,majorcode,degreetype) values (%s,%s,%s)',
#                 (item['schoolcode'], item['majorcode'], item['degreetype']))

class MajorPipeline(object):
    def __init__(self):
        dbargs = dict(
            host = '47.93.225.12',
            db = 'school-matriculate',
            user = 'zkrt',  # replace with you user name
            passwd = 'zkrtFCZ812',  # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item
    def insert_into_table(self,conn,item):
        conn.execute(
                'insert into majorname_majorcode(majorname,majorcode) values (%s,%s)',
                (item['majorname'], item['majorcode']))

class SchoolInfoPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='47.93.225.12',
            db='school-matriculate',
            user='zkrt',  # replace with you user name
            passwd='zkrtFCZ812',  # replace with you password
            port=3306,
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, schoolInfo_items, spider):
        try:

            sql = "insert into `school_info` (`school_name_cn`,`school_name_en`,`schoolcode`,`abbreviation`," \
                  "`province`,`city`,`grade`,`buildtime`,`category`,`type`,`ascription`,`address`," \
                  "`tel`,`summary`,`website`,`alumni`,`motto`,`logo`,`picture`,`keydiscipline`," \
                  "`ranking`) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (schoolInfo_items['school_name_cn'], schoolInfo_items['school_name_en'], schoolInfo_items['schoolcode'],
                   schoolInfo_items['abbreviation'], schoolInfo_items['province'],schoolInfo_items['city'],
                   schoolInfo_items['grade'], schoolInfo_items['buildtime'],

                   schoolInfo_items['category'], schoolInfo_items['type'], schoolInfo_items['ascription'],
                   schoolInfo_items['address'], schoolInfo_items['tel'],schoolInfo_items['summary'],
                   schoolInfo_items['website'], schoolInfo_items['alumni'],

                   schoolInfo_items['motto'], schoolInfo_items['logo'], schoolInfo_items['picture'],
                   schoolInfo_items['keydiscipline'], schoolInfo_items['ranking'])

            self.cursor.execute(sql)

            self.connect.commit()
        except pymysql.Error as error: #pymysql.Error
            sql = "insert into `school_info` (`school_name_cn`,`school_name_en`,`schoolcode`,`abbreviation`," \
                  "`province`,`city`,`grade`,`buildtime`,`category`,`type`,`ascription`,`address`," \
                  "`tel`,`summary`,`website`,`alumni`,`motto`,`logo`,`picture`,`keydiscipline`," \
                  "`ranking`) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (schoolInfo_items['school_name_cn'], schoolInfo_items['school_name_en'],
                   schoolInfo_items['schoolcode'],
                   schoolInfo_items['abbreviation'], schoolInfo_items['province'], schoolInfo_items['city'],
                   schoolInfo_items['grade'], schoolInfo_items['buildtime'],

                   schoolInfo_items['category'], schoolInfo_items['type'], schoolInfo_items['ascription'],
                   schoolInfo_items['address'], schoolInfo_items['tel'], schoolInfo_items['summary'],
                   schoolInfo_items['website'], schoolInfo_items['alumni'],

                   schoolInfo_items['motto'], schoolInfo_items['logo'], schoolInfo_items['picture'],
                   schoolInfo_items['keydiscipline'], schoolInfo_items['ranking'])
            with open('error.txt', 'a', encoding='gbk') as f:
                f.write(sql+'\n')
                f.write(str(error)+'\n')
                f.close()
            # logging.error(error)
        return schoolInfo_items

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

class ScoreSchoolMajorPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='47.93.225.12',
            db='school-matriculate',
            user='zkrt',  # replace with you user name
            passwd='zkrtFCZ812',  # replace with you password
            port=3306,
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, score_school_major_items, spider):
        try:

            sql = "insert into `score_school_major` (`schoolcode`,`majorcode`,`year`,`type`,`category`,`batch`,`highestscore`,`lowestscore`)" \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (score_school_major_items['schoolcode'], score_school_major_items['majorcode'], score_school_major_items['year'],
                   score_school_major_items['type'], score_school_major_items['category'],score_school_major_items['batch'],
                   score_school_major_items['highestscore'], score_school_major_items['lowestscore'],
                   )

            self.cursor.execute(sql)

            self.connect.commit()
        except pymysql.Error as error: #pymysql.Error
            sql = "insert into `score_school_major` (`schoolcode`,`majorcode`,`year`,`type`,`category`,`batch`,`highestscore`,`lowestscore`,)" \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (score_school_major_items['schoolcode'], score_school_major_items['majorcode'],
                   score_school_major_items['year'],
                   score_school_major_items['type'], score_school_major_items['category'],
                   score_school_major_items['batch'],
                   score_school_major_items['highestscore'], score_school_major_items['lowestscore'],
                   )
            with open('error.txt', 'a', encoding='gbk') as f:
                f.write(sql+'\n')
                f.write(str(error)+'\n')
                f.close()
            # logging.error(error)
        return score_school_major_items

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()