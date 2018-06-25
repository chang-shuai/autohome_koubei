import scrapy
import json
from autohome_koubei.items import AutohomeKoubeiItem
from datetime import date


class KoubeiSpider(scrapy.Spider):
    name = "koubei_spider"

    start_urls = [
        "https://koubei.app.autohome.com.cn/autov9.1.0/alibi/NewEvaluationInfo.ashx?eid=2077290&useCache=1",
    ]

    def parse(self, response):
        data = json.loads(response.text)
        result = data["result"]

        item = AutohomeKoubeiItem()
        item["series_id"] = str(result["seriesid"])
        item["series_name"] = result["seriesname"]
        item["user_id"] = str(result["userId"])
        item["user_name"] = result["userName"]
        item["release_date"] = result["LastAppendString"]
        item["purchasing_date"] = result["boughtdate"]
        item["model"] = result["specname"]
        item["purchase_place"] = result["boughtcityname"]
        item["dealer"] = result["dealername"]
        item["naked_car"] = result["boughtPrice"]
        item["average_fuel_consumption"] = result["actualOilConsumption"]
        item["road_haul"] = result["drivekilometer"]
        item["grade_facade"] = result["apperanceScene"]["score"]
        item["grade_trim"] = result["internalScene"]["score"]
        item["grade_space"] = result["spaceScene"]["score"]
        item["grade_impetus"] = result["powerScene"]["score"]
        item["grade_control"] = result["maneuverabilityScene"]["score"]
        item["grade_oil_wear"] = result["oilScene"]["score"]
        item["grade_comfort"] = result["comfortablenessScene"]["score"]
        item["grade_cost_performance"] = result["costefficientScene"]["score"]
        item["page_url"] = response.url
        item["discuss_title"] = result["summary"]
        item["discuss_merit"] = result["bestScene"]["feeling"]
        item["discuss_defect"] = result["worstScene"]["feeling"]
        item["discuss_facade"] = result["apperanceScene"]["feeling"]
        item["discuss_trim"] = result["internalScene"]["feeling"]
        item["discuss_space"] = result["spaceScene"]["feeling"]
        item["discuss_price"] = result["costefficientScene"]["feeling"]
        item["discuss_impetus"] = result["powerScene"]["feeling"]
        item["discuss_control"] = result["maneuverabilityScene"]["feeling"]
        item["discuss_oil_wear"] = result["oilScene"]["feeling"]
        item["discuss_comfort"] = result["comfortablenessScene"]["feeling"]
        item["discuss_why_choice"] = result["reasonScene"]["feeling"]
        item["update_date"] = str(date.today())

        yield item












if __name__ == '__main__':
    koubei = KoubeiSpider()
