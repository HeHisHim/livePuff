from collections import defaultdict
import datetime

import pandas as pd
import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()

MAIN_PAGE = "https://h5.jiangduoduo.com/list/1001?frm=C_ALADDIN&iss=20050"
WHICH_DAY_MAP = {
    "星期四": "Thursday",
    "星期二": "Tuesday",
    "星期日": "Sunday"
}


def get_page_info():
    info = requests.get(MAIN_PAGE, verify=False)
    info.encoding = "utf-8"
    info_text = info.text
    structure = etree.HTML(info_text)
    ball_list = structure.xpath('//div[@class="card-box"]')
    ball_list = ball_list[1:]
    return ball_list


def cal_date(dt_text):
    dt_text = dt_text.strip()
    dt_text = dt_text.replace(" ", "").replace("]", "")
    dt, which_day = dt_text.split("[")
    dt = datetime.datetime.strptime(dt, "%Y-%m-%d").date()
    year, month, day = dt.year, dt.month, dt.day
    dt_key = year * 10000 + month * 100 + day

    return dt_key, which_day


def cal_ball(ball_info):
    d = defaultdict(list)
    for element in ball_info:
        if not element.values():
            d["red"].append(int(element.text[1:]) if "0" == element.text[0] else int(element.text))
        else:
            d["blue"] = int(element.text[1:]) if "0" == element.text[0] else int(element.text)
    return d


def count_in_dict():
    all_in = {}
    ball_list = get_page_info()
    for target in ball_list:
        dt_text = target.xpath('div[@class="card-linetime"]/p[@class="card-week"]')[0].text
        dt_key, which_day = cal_date(dt_text)
        ball_info = target.xpath('div[@class="card-3dbox"]/div[@class="card-3dnum"]/em')
        red_blue = cal_ball(ball_info)
        red_blue["which_day"] = WHICH_DAY_MAP[which_day]
        all_in[dt_key] = red_blue

    return all_in


def analysis():
    all_in = count_in_dict()
    df = pd.DataFrame(all_in)
    df = df.T
    # print(df)
    print(df[df["which_day"] == "Tuesday"]["blue"].value_counts())
    print(len(df[df["which_day"] == "Tuesday"]))


if __name__ == "__main__":
    analysis()
