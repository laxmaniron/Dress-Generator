import time
from PIL import Image

import sys
import os
import io

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

content = sys.argv[1]
style = sys.argv[2]

name1 = "content__scale.jpg"
name2 = "style__scale.jpg"

im = Image.open(content).convert("RGB")
im = im.resize((762, 1100))
im.save(name1, "jpeg")

im1 = Image.open(style).convert("RGB")
im1 = im1.resize((762, 1100))
im1.save(name2, "jpeg")

cmd = 'matlab -nosplash -nodesktop -r "run(\'./binaryinverter.m\');exit;" '

returned_value = os.system(cmd)

print(returned_value)

time.sleep(20)

cmd = "python stylize.py --mask_n_colors=2 --content_img=./content__scale.jpg --target_mask=./content__mask.jpg --style_img=./style__scale.jpg --style_mask=./style__mask.jpg --content_weight=30 --iteration=800"

returned_value = os.system(cmd)
print(returned_value)
