#m7.8GetCSV2List.py
#导入CSV格式数据列表

fo = open("price2016.csv", "r")
ls = []
for line in fo:
    line = line.replace("\n", "")
    ls.append(line.split(","))
print(ls)
fo.close()
