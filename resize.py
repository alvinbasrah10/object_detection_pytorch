from PIL import Image
import os, sys

path = ("C:/Users/Andalabs-20/Documents/pytorch-yolo-v3/imgs/img/")
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((448,448), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=95)

resize()