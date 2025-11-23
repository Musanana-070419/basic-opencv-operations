import cv2
import numpy as np
import math

def generate_golden_spiral_galaxy():
    # --- 1. 设置画布 ---
    WIDTH, HEIGHT = 800, 800
    # 纯黑背景，凸显色彩
    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    CX, CY = WIDTH // 2, HEIGHT // 2

    # --- 2. 参数设置 ---
    # 点的数量：越多越细腻，像星尘一样
    num_points = 3000 
    # 扩散参数：决定了点之间的间距
    c = 6.5 
    # 黄金角度 (弧度制)
    # 137.508... 度是自然界最神秘的数字，保证点永远不重叠
    golden_angle = 137.508 * (math.pi / 180.0)

    print(f"正在生成 {num_points} 个星尘粒子...")

    # --- 3. 循环绘制每一个点 ---
    for n in range(num_points):
        # [核心数学逻辑]
        # 角度 = n * 黄金角
        theta = n * golden_angle
        # 半径 = c * sqrt(n) (这是让点均匀分布的关键公式)
        r = c * math.sqrt(n)

        # 转换为直角坐标
        x = int(CX + r * math.cos(theta))
        y = int(CY + r * math.sin(theta))

        # [色彩魔法]
        # 我们让颜色随着角度(theta)和半径(r)同时变化
        # 这样会形成旋转的彩虹色带
        
        # 色相 (Hue): 0-179
        # (theta % 2pi) 决定了旋转的颜色变化
        # (r * 0.2) 决定了从里到外的颜色变化
        hue = int((theta * 20 + r * 0.5)) % 180
        
        # 饱和度 (Saturation): 越往外越鲜艳
        saturation = int(min(255, 100 + r * 0.5))
        
        # 亮度 (Value): 255
        value = 255

        # 转为 BGR
        hsv_color = np.uint8([[[hue, saturation, value]]])
        bgr_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)[0][0]
        
        # 强制转为 int tuple (防止报错)
        color = (int(bgr_color[0]), int(bgr_color[1]), int(bgr_color[2]))

        # [绘制点]
        # 点的大小随着距离变大一点点，增加立体感
        radius_size = 1
        if n > 2000: radius_size = 3
        elif n > 1000: radius_size = 2
        
        cv2.circle(img, (x, y), radius_size, color, -1, cv2.LINE_AA)

    return img

if __name__ == '__main__':
    try:
        galaxy_img = generate_golden_spiral_galaxy()
        
        cv2.imshow('Golden Spiral Galaxy', galaxy_img)
        
        print("绘制完成。")
        print("这是一种基于自然界‘黄金分割’定律的图案，看起来应该顺眼多了！")
        print("按任意键退出。")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")