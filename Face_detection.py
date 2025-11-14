# Get XML file from opencv github for harr_cascade
# Face detection (Group/single person)

import cv2 as cv

img = cv.imread(r'<File name/directory>')
cv.imshow('<Image of how many people>', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray <People>', gray)

haar_cascade = cv.CascadeClassifier('harr_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=9)
cv.imshow('Detected Faces', img)

cv.waitKey(0)
