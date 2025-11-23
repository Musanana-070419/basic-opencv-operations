import cv2
import numpy as np

#读取图像
img = cv2.imread ("cube.jpg")

#灰度化
gray = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)

# 创建一个 CLAHE 对象 
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
# 应用到灰度图上
gray = clahe.apply(gray)

#读取转角处
corner = cv2.goodFeaturesToTrack ( gray , 200 , 0.01 , 200)

#坐标转整数
corner = np.int64 (corner)

#创建副本图像
img_copy = img.copy ()

#解压绘制
for i in corner:

    x, y = i.ravel ()


    cv2.circle (img_copy , (x,y) , 20 , (0, 0 ,255) , -1)

#显示图像
# 1. 创建一个名字叫 'Result' 的窗口
# cv2.WINDOW_NORMAL = 允许手动拖拽改变窗口大小
cv2.namedWindow('Result', cv2.WINDOW_NORMAL) 

# 2. (可选) 强制把这个窗口设定成你想要的大小，比如 800x600
cv2.resizeWindow('Result', 800, 600)

# 3. 在这个窗口里显示图片
# 注意：这里的窗口名字 'Result' 必须和上面的一模一样！
cv2.imshow('Result', img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
