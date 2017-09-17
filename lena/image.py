
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=np.array(Image.open('g:/lena.jpg').convert('L'))

rows,cols=img.shape
for i in range(rows):
    for j in range(cols):
        print(img[i,j])
         
plt.figure("lena")
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()
