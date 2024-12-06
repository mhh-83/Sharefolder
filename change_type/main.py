from PIL import Image
import os

root = r"D:/"
count = 0
for dirs, subdirs, files in os.walk(root):
    for file in files:
        last = file[-1:]
        if(last == "jfif"):
            img = Image.open(root + "//"+file)
            filename = file[:-4]
            img.save(root + "//"+filename + "jpg")