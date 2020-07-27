from datetime import datetime

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

COLUMN_MAP = {
    "货币名称": "symbol",
    "现汇买入价": "buying_rate",
    "现钞买入价": "cash_buying_rate",
    "现汇卖出价": "selling_rate",
    "现钞卖出价": "cash_selling_rate",
    "发布日期": "trading_date",
    "发布时间": "trading_time"
}


class ExchangeRate:

    TARGET_URL = "https://www.boc.cn/sourcedb/whpj/"
    FOCUS = ("港币", "美元", "英镑", )

    def __init__(self) -> None:
        self.table = pd.read_html(self.TARGET_URL)[1]
        self.table = self.table[COLUMN_MAP.keys()]
        self.table.rename(columns=COLUMN_MAP, inplace=True)
        self.table["trading_date"] = self.table["trading_date"].apply(lambda x: datetime.strptime(x, "%Y.%m.%d %H:%M:%S").date())
        self.table["trading_time"] = self.table["trading_time"].apply(lambda x: datetime.strptime(x, "%H:%M:%S").time())
        self.table = self.table[self.table["symbol"].isin(self.FOCUS)]
        self.table.reset_index(inplace=True, drop=True)

    def data(self):
        print(self.table)
        x = self.table["trading_time"][0]
        print(x, type(x))

    def get_time(self):
        curr_time = self.structure.xpath("//p[@class='sort_time clearfix']")
        print(curr_time)


if "__main__" == __name__:
    handler = ExchangeRate()
    handler.data()
