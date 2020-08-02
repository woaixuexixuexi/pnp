import cv2
import numpy as np
from math import atan2, sqrt

# 创建摄像头捕获模块
cap = cv2.VideoCapture(0)

# 创建窗口
window_handle = cv2.namedWindow("USB Camera", cv2.WINDOW_AUTOSIZE)

# 创建二维码检测器
qrDecoder = cv2.QRCodeDetector()

i = 0

#世界坐标系位置
object_3d_points = np.array(([-67, 66.5, 0],
                             [67, 66.5, 0],
                             [67, -66.5, 0],
                             [-67, -66.5, 0]), dtype=np.float)
#内参矩阵
camera_matrix = np.array(([383.24421089, 0, 339.51310798],
                          [0, 383.12321954, 236.42845787],
                          [0, 0, 1.0]), dtype=np.float)
#畸变矩阵
dist_coefs = np.array([0.06804571, -0.21537906, -0.00031575, 0.00251214, 0.2158873], dtype=np.float)
# 逐帧显示
while cv2.getWindowProperty("USB Camera", 0) >= 0:
    ret_val, img = cap.read()
    # print(img.shape)

    # 图像太大需要调整
    height, width = img.shape[0:2]
    if width > 800:
        new_width = 800
        new_height = int(new_width / width * height)
        img = cv2.resize(img, (new_width, new_height))

    # 二维码检测和识别
    data, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)

    #相机坐标系位置
    object_2d_point = bbox


    if len(data) > 0:
        found, rvec, tvec = cv2.solvePnP(object_3d_points, object_2d_point, camera_matrix, dist_coefs)

        #输出二维码位置信息
        rotM = cv2.Rodrigues(rvec)[0]#solvePnP返回的raux是旋转向量，可通过罗德里格斯变换成旋转矩阵R。
        camera_postion = -np.matrix(rotM).T * np.matrix(tvec) #得出相机相对现实坐标系的坐标
        print("x,y,z轴位置：")
        print(camera_postion.T)#输出为 x,y,z轴信息

        #反解出相机在现实坐标系在绕各个轴的旋转角度，正数表示顺时针旋转
        theta_z = atan2(rotM[1][0], rotM[0][0])*57.2958;
        theta_y = atan2(-rotM[2][0], sqrt(rotM[2][0] * rotM[2][0] + rotM[2][2] * rotM[2][2]))*57.2958;
        theta_x = atan2(rotM[2][1], rotM[2][2])*57.2958;
        print("x,y,z轴的旋转角度:")
        print(theta_x, theta_y, theta_z)

        print("解码数据 : {}".format(data))
        n = len(bbox)
        for j in range(n):
            cv2.line(img, tuple(bbox[j][0]), tuple(bbox[(j + 1) % n][0]), (255, 0, 0), 3)
    else:
        i += 1
        if(i%20==0):
            print("没有检测到二维码")

    # 显示图像
    cv2.imshow("USB Camera", img)

    keyCode = cv2.waitKey(30) & 0xFF
    if keyCode == 27:  # ESC键退出
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()