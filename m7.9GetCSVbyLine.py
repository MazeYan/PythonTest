#m7.9GetCSVbyLine.py
#逐行处理CSV格式数据

fo = open("price2016.csv", "r")
ls = []
for line in fo:
    line = line.replace("\n"," ")
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns += "{}\t".format(s)
    print(lns)
fo.close()
