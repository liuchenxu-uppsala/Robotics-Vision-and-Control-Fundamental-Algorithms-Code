import cv2
import matplotlib.pyplot as plt

# 1. 读取两张图像（比如一张是物体，另一张是包含该物体的复杂场景）
img1 = cv2.imread('object.jpg', 0)  # 目标物体
img2 = cv2.imread('scene.jpg', 0)   # 场景图像

# 2. 初始化 SIFT 探测器
# 在你的机器人项目里，这一行代码就完成了你刚才学的“金字塔”和“128维描述子”的所有逻辑
sift = cv2.SIFT_create()

# 3. 找到关键点 (Keypoints) 和 描述子 (Descriptors)
# kp 是坐标、尺度、方向的集合；des 就是那 128 维的“身份证”数组
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# 4. 初始化匹配器 (BFMatcher - Brute Force Matcher)
# 我们使用欧氏距离 (NORM_L2) 来对比这 128 维向量
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2) # k=2 是为了找“最近”和“次近”的两个点

# 5. 应用 Lowe's Ratio Test（比值判别法）
# 只有当 最近距离 / 次近距离 < 0.75 时，我们才认为这个匹配是靠谱的
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append([m])

# 6. 画出匹配结果
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_matches, None, flags=2)

plt.imshow(img3)
plt.title("SIFT Feature Matching")
plt.show()