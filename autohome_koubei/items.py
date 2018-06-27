# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeKoubeiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    series_id = scrapy.Field()              # 车系id
    series_name = scrapy.Field()            # 车系名 
    user_id = scrapy.Field()                # 用户id 
    user_name = scrapy.Field()              # 用户名
    release_date = scrapy.Field()           # 发布时间
    purchasing_date = scrapy.Field()        # 购买时间
    model = scrapy.Field()                  # 车型
    purchase_place = scrapy.Field()         # 购买地点
    dealer_name = scrapy.Field()            # 经销商名
    naked_car = scrapy.Field()              # 购入裸车价
    average_fuel_consumption = scrapy.Field()   # 平均油耗
    road_haul = scrapy.Field()              # 行驶里程
    grade_facade = scrapy.Field()           # 外观评分
    grade_trim = scrapy.Field()             # 内饰评分
    grade_space = scrapy.Field()            # 空间评分
    grade_deploy = scrapy.Field()           # 配置评分
    grade_impetus = scrapy.Field()          # 动力评分
    grade_control = scrapy.Field()          # 控制评分
    grade_oil_wear = scrapy.Field()         # 油耗评分
    grade_comfort = scrapy.Field()          # 舒适评分
    grade_cost_performance = scrapy.Field() # 性价比评分
    page_url = scrapy.Field()               # 网页的URL

    discuss_title = scrapy.Field()          # 口碑标题
    discuss_merit = scrapy.Field()          # 最满意
    discuss_defect = scrapy.Field()         # 最不满意
    discuss_facade = scrapy.Field()         # 外观
    discuss_trim = scrapy.Field()           # 内饰
    discuss_space = scrapy.Field()          # 空间
    discuss_price = scrapy.Field()          # 性价比
    discuss_impetus = scrapy.Field()        # 动力
    discuss_control = scrapy.Field()        # 操控
    discuss_oil_wear = scrapy.Field()       # 油耗
    discuss_comfort = scrapy.Field()        # 舒适性
    discuss_why_choice = scrapy.Field()     # 为什么选这款车
    update_date = scrapy.Field()            # 更新日期


