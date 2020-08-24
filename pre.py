import rqdatac
from rqdatac.utils import to_date, to_date_str
from collections import defaultdict

MISS = ["009317"]

# 009300 <西部利得中证500指数增强(LOF)C>
# 008960 <长信国防军工量化灵活配置混合C>
# 007538 <永赢沪深300指数A> !!!
# 009011 <华夏睿阳一年持有期混合>
# 007539 <永赢沪深300指数C>
# 007657 <东方红中证竞争力指数A>
# 009057 <博时科技创新混合A>
# 008860 <民生加银龙头优选股票>
# 008112 <中泰中证500指数增强A>
# 009058 <博时科技创新混合C>
# 008477 <安信价值驱动三年持有期混合>
# 007658 <东方红中证竞争力指数C>
# 008113 <中泰中证500指数增强C>
# 007275 <银河沪深300指数增强A>

OK = ["009300", "008960", "007538", "009011", "007539", "007657", "009057", "008860", "008112", "009058", "008477", "007658", "008113", "007275"]


class Fund:
    def __init__(self):
        rqdatac.init(uri="tcp://rice:rice@192.168.10.11:17010")
        ins = rqdatac.fund.all_instruments()
        ins = ins["Money" != ins["fund_type"]]
        self.ids = list(ins["order_book_id"])
        self.data = []

    # 选择发行日期大于2019-06-30的基金
    def filter_date(self):
        target_date = to_date("2019-06-30")
        for i in self.ids:
            listed_date = to_date(rqdatac.fund.instruments(i).listed_date)
            de_listed_date = rqdatac.fund.instruments(i).de_listed_date
            if listed_date > target_date and "0000-00-00" == de_listed_date:
                self.data.append(i)

    def nv_data(self):
        self.filter_date()
        field = "acc_net_value"
        map_it = {}
        self.map_it_date = defaultdict(list)
        nv = rqdatac.fund.get_nav(self.data, expect_df=True)[[field]]
        nv.reset_index(inplace=True)
        groups = nv.groupby("order_book_id")
        for group in groups:
            o = group[0]
            if o in MISS:
                continue
            df = group[1][field]
            if float(df.iloc[-1]) > 1.35:
                continue
            df_date = group[1]["datetime"]
            self.map_it_date[o].append((df_date.iloc[0], df_date.iloc[-1]))
            map_it[o] = (float(df.iloc[-1]) - float(df.iloc[0])) / float(df.iloc[0])
        self.map_it_sort = sorted(map_it.items(), key=lambda x: x[1], reverse=True)
        self.map_it_sort = self.map_it_sort[:20]

    def print_it(self):
        self.nv_data()
        print()
        for it in self.map_it_sort:
            if it[0] not in OK:
                continue
            symbol = rqdatac.fund.instruments(it[0]).symbol
            print("{} <{}> 在 {}到{} 收益率 {}%".format(it[0], symbol, to_date_str(self.map_it_date[it[0]][0][0]), to_date_str(self.map_it_date[it[0]][0][1]), it[1] * 100))
            print()

    def print_it2(self):
        self.nv_data()
        for it in self.map_it_sort:
            symbol = rqdatac.fund.instruments(it[0]).symbol
            print("{} - {}".format(it[0], symbol))


if "__main__" == __name__:
    handler = Fund()
    handler.print_it()