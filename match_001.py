import cv2
import numpy as np

#读取并转化灰度图

img_matchtest = cv2.imread("poker.jpg")
gray = cv2.cvtColor (img_matchtest , cv2.COLOR_BGR2GRAY)

template = cv2.imread ("diamond_template.jpg",0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    
#设定匹配阈值
threshold = 0.9
    
# 找到所有大于阈值的点
loc = np.where(res >= threshold)

    # 标记结果
points = []
for pt in zip(*loc[::-1]):
        cv2.rectangle(img_matchtest, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('Template Match Result', img_matchtest)
cv2.waitKey(0)
cv2.destroyAllWindows()