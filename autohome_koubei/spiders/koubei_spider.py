import scrapy
import json

class KoubeiSpider(scrapy.Spider):
    name = "koubei_spider"

    start_urls = [
        "https://koubei.app.autohome.com.cn/autov9.1.0/alibi/NewEvaluationInfo.ashx?eid=2077290&useCache=1",
    ]

    def parse(self, response):
        print("#############请注意################")
        print(response.selector)
        #data = json.load(response.selector)


if __name__ == '__main__':
    koubei = KoubeiSpider()
