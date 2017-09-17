#-*-coding:utf-8-*-

"""
版本  :Python 2.7
编辑器:Sublime Text 3
标准库:urllib
作者  :Maze
"""
import urllib

url = "http://www.163.com/"



# print html.read().decode("gbk").encode("utf-8")

urllib.urlretrieve(url,"d:\\abc.txt")




