import cv2

#截取图片
cap = cv2.VideoCapture(0)
cv2.namedWindow("My Capture",cv2.WINDOW_NORMAL)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,-3)
i=0

#相机参数
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FPS,60)
while cap.isOpened():
    flag,frame = cap.read()
    if flag:
        cv2.imshow("My Capture",frame)
    # 下面这段代码：按下ESC键退出
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        bre1ak
    fileName = 'image'+str(i)+'.jpg'
    #按 z 键保存图片
    if k == ord('z'):
        cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        i += 1
        print('截取第%d张图片'%i)

cap.release()
cv2.destroyAllWindows()

'''
#实时显示视频
cap = cv2.VideoCapture(0)
cv2.namedWindow("My Capture",cv2.WINDOW_NORMAL)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,-1)
while cap.isOpened():
    flag,frame = cap.read()
    if flag:
        cv2.imshow("My Capture",frame)
#下面这段代码：按下ESC键退出
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
'''
'''
#视频播放录制
cap = cv2.VideoCapture(0)
cap.set(3,720)
#cv2.namedWindow("My Capture",cv2.WINDOW_NORMAL)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))#获取图片大小
fps = 60   #保存视频帧数， 实时显示的帧数和视频保存的帧数不同
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vout = cv2.VideoWriter()
vout.open('output.mp4',fourcc,fps,size,True)
while cap.isOpened():
    flag,frame = cap.read()
    if flag:
        cv2.imshow("My Capture",frame)
#下面这段代码：按下ESC键退出
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    #cv2.putText(frozenset,str(i),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1,cv2.LINE_AA)
    vout.write(frame)

cap.release()
vout.release()
cv2.destroyAllWindows()
'''