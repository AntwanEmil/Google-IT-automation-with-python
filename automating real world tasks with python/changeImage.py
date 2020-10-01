#!/usr/bin/env python3

import os,glob
from PIL import Image

#making jpegs :D
path = "supplier-data/images"
for f in os.listdir(path):
    if f.endswith(".DS_Store"):
        continue
    if f.endswith(".tiff"):
        i = Image.open(f)
        i = i.convert("RGB")
        fn,fext = os.path.splitext(f)
        i.resize((600,400)).save("{}.jpeg".format(fn))

        

#deleting .TIFFs
for f in os.listdir(path):
    if f.endswith(".jpeg"):
        continue
    else:
        os.remove(f)


