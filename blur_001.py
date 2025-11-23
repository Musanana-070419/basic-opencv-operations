import cv2

#读取图像
img = cv2.imread ("plane.jpg")

#中值滤波
median = cv2.medianBlur (img , 5)

#高斯滤波
gaussian = cv2.GaussianBlur (img , (5 ,5), 0)

#显示图像
cv2.imshow ("original img",img)
cv2.imshow ("median img",median)
cv2.imshow ("gaussian img",gaussian)

print ("滤波完成")
print ("按任意键关闭所有图像窗口")

cv2.waitKey (0)
cv2.destroyAllWindows ()

