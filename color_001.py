import cv2


# 读取图像
image = cv2.imread("RGB.jpg")

# 颜色通道顺序
cv2.imshow("blue", image[:, :, 0])
cv2.imshow("green", image[:, :, 1])
cv2.imshow("red", image[:, :, 2])

#灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)


cv2.waitKey(0)