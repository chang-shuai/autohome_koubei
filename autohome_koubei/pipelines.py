# -*- coding: utf-8 -*-
import psycopg2
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutohomeKoubeiPipeline(object):

    def __init__(self, kargs):
        self.conn = psycopg2.connect(database=kargs["pg_dbname"], user=kargs["pg_user"], password=kargs["pg_password"], host=kargs["pg_host"], port=kargs["pg_port"])
        self.cursor = self.conn.cursor()
        self.koubei_sql = """INSERT INTO autohome_koubei.user_koubei
                        (user_id,
                        series_id,
                        series_name,
                        release_date,
                        discuss_title,
                        discuss_merit,
                        discuss_defect,
                        discuss_facade,
                        discuss_trim,
                        discuss_space,
                        discuss_price,
                        discuss_impetus,
                        discuss_control,
                        discuss_oil_wear,
                        discuss_comfort,
                        discuss_why_choice,
                        update_date)
                        VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        self.score_sql = """INSERT INTO autohome_koubei.user_score(
                        series_id,
                        user_id,
                        user_name,
                        release_date,
                        purchasing_date,
                        model,
                        purchase_place,
                        dealer_name,
                        naked_car,
                        average_fuel_consumption,
                        road_haul,
                        grade_facade,
                        grade_trim,
                        grade_space,
                        grade_impetus,
                        grade_control,
                        grade_oil_wear,
                        grade_comfort,
                        grade_cost_performance,
                        update_date)
                        VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""


    @classmethod
    def from_crawler(cls, crawler):
        pg_param = dict(
				pg_host = crawler.settings.get("PG_HOST"),
				pg_port = crawler.settings.get("PG_PORT"),
				pg_user = crawler.settings.get("PG_USER"),
				pg_password = crawler.settings.get("PG_PASSWORD"),
				pg_dbname = crawler.settings.get("PG_DBNAME"),
			)
        return cls(pg_param)

    def process_item(self, item, spider):
        self.cursor.execute(self.koubei_sql, (item["user_id"], item["series_id"], item["series_name"], item["release_date"], item["discuss_title"], item["discuss_merit"], item["discuss_defect"], item["discuss_facade"], item["discuss_trim"], item["discuss_space"], item["discuss_price"], item["discuss_impetus"], item["discuss_control"], item["discuss_oil_wear"], item["discuss_comfort"], item["discuss_why_choice"], item["update_date"]))
        self.cursor.execute(self.score_sql, (item["series_id"], item["user_id"], item["user_name"], item["release_date"], item["purchasing_date"], item["model"], item["purchase_place"], item["dealer_name"], item["naked_car"], item["average_fuel_consumption"], item["road_haul"], item["grade_facade"], item["grade_trim"], item["grade_space"], item["grade_impetus"], item["grade_control"], item["grade_oil_wear"], item["grade_comfort"], item["grade_cost_performance"], item["update_date"]))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()