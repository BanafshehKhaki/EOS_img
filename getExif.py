import os,sys
from PIL import Image
from PIL.ExifTags import TAGS
import math
import re

runNames =['1mgrun1']
# ,'1mgrun2',
# '1mgrun3',
# '1mgrun4',
# '1mgrun5',
# '5mgrun1',
# '5mgrun2',
# '5mgrun3',
# '5mgrun4',
# '5mgrun5',
# '10mgrun1attempt2',
# '10mgrun2',
# '10mgrun3',
# '10mgrun4',
# '10mgrun5']

for run in runNames:
    dash ='/'
    recordFile = open("exif_data_"+run+"testt.txt",'w')
    files = [f for f in os.listdir('EOS_imgs/'+run+dash) if f.endswith(".JPG")]
    
    for file in files:
        img_path = "EOS_imgs/"+run+dash+file
        i = Image.open(img_path)
       	info = i._getexif()
       	for tag, value in info.items():
       		decoded = TAGS.get(tag, tag)
       		if decoded != "MakerNote":
       			recordFile.write(decoded + " " + str(value)+" " + str(tag)+"\n")
       	recordFile.write('\n')
    recordFile.close()