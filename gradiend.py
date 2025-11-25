import cv2
import os

gray = cv2.imread("ball.png", cv2.IMREAD_GRAYSCALE)



#高斯拉普拉斯算子
Gossian = cv2.GaussianBlur(gray, (3, 3), 0)
laplacian1 = cv2.Laplacian(Gossian, cv2.CV_64F)
laplacian2 = cv2.Laplacian(gray, cv2.CV_64F)
cv2.imshow("laplacian2", laplacian2)
cv2.imshow("laplacian",laplacian1 )

#sobel算子
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow("sobelx", sobelx)
cv2.imshow("sobely", sobely)

#canny算子
canny = cv2.Canny(gray, 180, 280)
cv2.imshow("canny", canny)
output_filename = "result_" + os.path.basename("ball.jpg")
output_img = canny.copy ()
cv2.imwrite(output_filename, output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
