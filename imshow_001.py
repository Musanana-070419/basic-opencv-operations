import cv2

#读取版本
print(cv2.getVersionString())
#读取图像
image = cv2.imread("miku001.jpg")
#图像数据
print(image.shape)

#显示图像
cv2.imshow("miku001", image)
cv2.waitKey(0)

