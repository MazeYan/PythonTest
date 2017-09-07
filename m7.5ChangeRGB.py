#m7.5ChangeRGB.py
#图像的颜色变换

from PIL import Image
im = Image.open("birdnest.jpg")
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save("birdnestRGB.jpg")
