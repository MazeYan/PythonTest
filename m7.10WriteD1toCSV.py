#m7.10WriteD1toCSV.py
#一维数据写入CSV文件

fo = open("price2016.csv", "w")
ls = ['北京', '1015', '120.7', '121.4']
fo.write(",".join(ls)+"\n")
fo.close()
