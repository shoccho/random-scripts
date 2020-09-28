import zipfile
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#change this imgzip to your desired Zip
imgzip = open('img.zip', 'rb')
z = zipfile.ZipFile(imgzip)
infolist = z.infolist()

for f in infolist:
    ifile = z.open(f)
    img = Image.open(ifile)
    open_cv_image = np.array(img)
    cimg = open_cv_image[:, :, ::-1].copy()
    gray_img = cv.cvtColor(cimg,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(cimg,1.3,5)
    ls=[]
    xx=0
    yy=0
    v=img.width
    for (x,y,w,h) in faces:
        d=img.crop((x,y,x+w,y+h))
        ls.append(d)
    if len(faces)>0:
        contact_sheet=Image.new(img.mode,(ls[0].width*5,ls[0].width*2))
    for d in ls:
        d.thumbnail((ls[0].width,ls[0].height))
        contact_sheet.paste(d,(xx,yy))
        xx+=ls[0].width
        if(xx>=contact_sheet.width):
            xx=0
            yy+=ls[0].height
    if len(faces)==0:
        print("There were no faces in that file")
    else:
        display(contact_sheet)
