# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LuluItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    provincename = scrapy.Field()
    provincecode = scrapy.Field()
    description = scrapy.Field()
    # inserttime = scrapy.Field()
    # updatetime = scrapy.Field()

    # pass

class DynamicItem(scrapy.Item):
    schoolcode = scrapy.Field()
    majorcode = scrapy.Field()
    degreetype = scrapy.Field()
    href = scrapy.Field()
    schoolname = scrapy.Field()
    majorname = scrapy.Field()


class MajorItem(scrapy.Item):
    majorname = scrapy.Field()
    majorcode = scrapy.Field()
    schoolname = scrapy.Field()

class SchoolInfoItem(scrapy.Item):
    school_name_cn = scrapy.Field()
    school_name_en = scrapy.Field()
    schoolcode = scrapy.Field()
    abbreviation = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    grade = scrapy.Field()
    buildtime = scrapy.Field()
    category = scrapy.Field()
    type = scrapy.Field()
    ascription = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()
    summary = scrapy.Field()
    website = scrapy.Field()
    alumni = scrapy.Field()
    motto = scrapy.Field()
    logo = scrapy.Field()
    picture = scrapy.Field()
    keydiscipline = scrapy.Field()
    ranking = scrapy.Field()


class ScoreSchoolMajorItem(scrapy.Item):
    schoolcode = scrapy.Field()
    majorcode = scrapy.Field()
    year = scrapy.Field()
    type = scrapy.Field()
    category = scrapy.Field()
    batch = scrapy.Field()
    highestscore = scrapy.Field()
    lowestscore = scrapy.Field()
