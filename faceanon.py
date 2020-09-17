import numpy as np
import cv2 as cv
import math
import time
from PIL import Image

def image_mask(input_img_array,mask_img_array,face_haar="haarcascade_frontalface_default.xml",eyes_haar="haarcascade_eye.xml"):
    output_image=[]
    img = Image.fromarray(input_img_array, 'RGB')
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
    mask=Image.fromarray(mask_img_array, 'RGB')  
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (fx,fy,fw,fh) in faces:                
        eyes = eye_cascade.detectMultiScale(img_gray[fy:fy+fh, fx:fx+fw])        
        eye_mid_x=eye_mid_y=[-1,-1]
        eyecount=0
        for (ex,ey,ew,eh) in eyes:                        
            eye_mid_x[eyecount]=(ex+ew)/2
            eye_mid_y[eyecount]=(ey+eh)/2
            eyecount=eyecount+1            
        mask_overlay = cv.resize(mask,(fw,fh),interpolation = cv.INTER_CUBIC)        
        angle_of_rotation=math.atan(float(eye_mid_y[1]-eye_mid_y[0])/(float(eye_mid_x[1]-eye_mid_x[0])+0.000001))                  
        mask_overlay_gray= cv.cvtColor(mask_overlay, cv.COLOR_BGR2GRAY)
        tmp_rows,tmp_cols = mask_overlay_gray.shape
        M = cv.getRotationMatrix2D((tmp_cols/2,tmp_rows/2),angle_of_rotation,1.0)
        overlay_final = cv.warpAffine(mask_overlay,M,(tmp_cols,tmp_rows),cv.BORDER_CONSTANT, borderValue=(255,255,255))
        mask_gray = cv.cvtColor(overlay_final, cv.COLOR_BGR2GRAY)
        overlay(fx,fy,fw,fh,mask_gray,img,mask_overlay,output_image)
        return np.asarray(Image.open(img))
    
def video_mask(input_file="input.avi",output_file="output.avi",mask_img_array,face_haar="haarcascade_frontalface_default.xml",eyes_haar="haarcascade_eye.xml",dimen1=848,dimen2=480):
    fourcc = cv.VideoWriter_fourcc(*'MJPG')
    out = cv.VideoWriter(output_file,fourcc, 20.0, (dimen1,dimen2))## output video file 
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
    mask=Image.fromarray(mask_img_array, 'RGB')
    cap = cv.VideoCapture(input_file) ## input video file
    while cap.isOpened():
        ret, img = cap.read()
        mask_gray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (fx,fy,fw,fh) in faces:                
            eyes = eye_cascade.detectMultiScale(img_gray[fy:fy+fh, fx:fx+fw])        
            eye_mid_x=eye_mid_y=[-1,-1]
            eyecount=0
            for (ex,ey,ew,eh) in eyes:                            
                eye_mid_x[eyecount]=(ex+ew)/2
                eye_mid_y[eyecount]=(ey+eh)/2
                eyecount=eyecount+1                            
            mask_overlay = cv.resize(mask,(fw,fh),interpolation = cv.INTER_CUBIC)        
            angle_of_rotation=math.atan(float(eye_mid_y[1]-eye_mid_y[0])/(float(eye_mid_x[1]-eye_mid_x[0])+0.000001))                  
            mask_overlay_gray= cv.cvtColor(mask_overlay, cv.COLOR_BGR2GRAY)
            tmp_rows,tmp_cols = mask_overlay_gray.shape
            M = cv.getRotationMatrix2D((tmp_cols/2,tmp_rows/2),angle_of_rotation,1.0)
            overlay_final = cv.warpAffine(mask_overlay,M,(tmp_cols,tmp_rows),cv.BORDER_CONSTANT, borderValue=(255,255,255))
            mask_gray = cv.cvtColor(overlay_final, cv.COLOR_BGR2GRAY)
            overlay(fx,fy,fw,fh,mask_gray,img,mask_overlay,output_file)        
        out.write(img)      
    cap.release()
    out.release()




def overlay(fx,fy,fw,fh,mask_gray,img,replacement_roi,output_file):
    for i in range(fh):
            for j in range(fw):
                if mask_gray[i][j]>235:
                    continue
                else:
                    img[fy+i][fx+j]=replacement_roi[i][j]
    

