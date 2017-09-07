#m7.4GifExtractor.py
#GIF文件图像提取

from PIL import Image
im = Image.open("pybit.gif")

try:
    im.save("picframe{:02d}.png".format(im.tell())) #tell()   返回当前帧的序号
    while True:
        im.seek(im.tell()+1)
        im.save("picframe{:02d}.png".format(im.tell()))
except:
    print("处理结束")
