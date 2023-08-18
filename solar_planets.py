import cv2

img=cv2.imread("./assests/solar-system.jpg")
cv2.putText(img," - SUN",(60,380),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))
cv2.putText(img,"MERCURY",(100,270),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))
cv2.putText(img,"VENUS",(190,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))
cv2.putText(img,"EARTH",(280,270),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))
cv2.putText(img,"MARS",(370,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))
cv2.putText(img,"JUPITER",(550,390),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))
cv2.putText(img,"SATURN",(760,330),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))
cv2.putText(img,"URANUS",(950,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))
cv2.putText(img,"NEPTUNE",(1100,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(225,225,225))

cv2.imshow("./assests/solar-system.jpg",img)
cv2.waitKey(5000)

cv2.imwrite("./assests/solar_systemwithname.jpg",img)