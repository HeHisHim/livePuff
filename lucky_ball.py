def fun(li):
    li_1 = []  # 接收value值
    li_2 = []  # 接收新的字典
    dict_1 = {}
    for i in range(len(li)):
        li_1.append(li[i]["key"])
    li_1.sort()  # 排序
    for i in li_1:
        dict_1 = {"key": i}
        print(dict_1)
        li_2.append(dict_1)
    return li_2

li = [{"key": 5}, {"key": 9}, {"key": -1}, {"key": 4}]
li.sort(key=lambda x: x["key"])
print(li)
