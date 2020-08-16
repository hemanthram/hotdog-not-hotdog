import filetype
import cv2
import os
import shutil

c = 0
invalid_img = cv2.imread('unavailable.jpg')
path = './nothotdog/people/'
invalids = []
for img in os.listdir(path):
    if(img == 'invalid'):
        continue
    ret = filetype.guess(path+'/'+img)
    if(ret == None):
        c += 1
        invalids.append(path+'/'+img)
        continue
    mat = cv2.imread(path+'/'+img)
    # print(img)
    try:
        if(mat.shape == invalid_img.shape):
            if((mat == invalid_img).all()):
                c += 1
                invalids.append(path+'/'+img)
    except:
        c += 1
        invalids.append(path+'/'+img)
    
print(len(invalids), "files found")
for inv in invalids:
    shutil.move(inv, path+'invalid/')

print(c)