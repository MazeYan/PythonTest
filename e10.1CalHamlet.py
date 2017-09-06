#e10.1CalHamlet.py
def getText():
    txt = open("hamlet.txt").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\}^_`{|}~':
        txt = txt.replace(ch, " ")  #将文本中特殊字符替换为空格
    return txt
hamletText = getText()
    
