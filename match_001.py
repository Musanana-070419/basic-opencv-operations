import cv2
import numpy as np

#转化灰度图
img = cv2.imread ("poker.jpg")
gray = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)

#模板匹配
tem = gray [65:110,230:270]
match = cv2.matchTemplate ( gray ,tem ,cv2.TM_CCOEFF_NORMED)
locations = np.where (match >= 0.9)

#画图
h ,w = tem.shape[0:2]
for p in zip (*locations[::-1]):
    x1,y1 =p [0],p [1]
    x2,y2 =x1 +w,y1 +h
    cv2.rectangle(img , (x1 ,y1),(x2 ,y2),(0,255,0), 2)

cv2.imshow ("match_test" , img)
cv2.waitKey()