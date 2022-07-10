# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:18:26 2022

@author: Asazad
"""

import cv2
import numpy as np
import face_recognition as fc

from simple_facerec import SimpleFacerec

sfr=SimpleFacerec()
sfr.load_encoding_images("./images/")

cap=cv2.VideoCapture(0)

while True:
    rect,frame=cap.read()
    face_location,face_names =sfr.detect_known_faces(frame)
    for face_loc,name in zip(face_location,face_names):
        top,left,bottom,right=face_loc[0],face_loc[1],face_loc[2],face_loc[3]
        cv2.putText(frame,name,(right,top-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),2)

    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()

cv2.destroyAllWindows()
