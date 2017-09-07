#m7.1DiffTextBin.py
#理解文本文件和二进制文件的区别

textFile = open("The Zen of Python.txt","rt") #t表示文本文件方式
print(textFile.readline())
textFile.close()
textFile = open("The Zen of Python.txt","rb") #b表示二进制文件方式
print(textFile.readline())
textFile.close()
