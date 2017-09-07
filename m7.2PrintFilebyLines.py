#m7.2PrintFilebyLines.py
#文本文件逐行打印

fname = input("请输入要打开的文件：")
fo = open(fname, "r")
for line in fo.readlines():
    print(line)
fo.close()
