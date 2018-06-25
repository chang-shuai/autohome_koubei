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
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()