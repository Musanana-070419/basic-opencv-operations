import cv2

#读取图像

image = cv2.imread("miku001.jpg")

#裁剪图像
cropped_image = image[0:1000, 0:1000]

#显示裁剪后的图像
cv2.imshow("Cropped Miku", cropped_image)
cv2.waitKey(0)
