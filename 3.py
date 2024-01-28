import cv2
vedio = cv2.VideoCapture("video (2160p).mp4")
out = cv2.imread("OIP.jpeg")
i=0
option=2  # 1 fro fast,2 for slow
while True:
    i+=1
    ret, frame = vedio.read()
    if i%3==0:
        frame1=cv2.resize(out,(int(frame.shape[1]*0.3),int(frame.shape[0]*0.3)),interpolation=cv2.INTER_AREA)
    else:
        frame1=cv2.resize(frame,(int(frame.shape[1]*0.3),int(frame.shape[0]*0.3)),interpolation=cv2.INTER_AREA)
    if not ret:
        break
    if option==1:
        for _ in range(3):
            vedio.read()
    elif option==2:
        for _ in range(3):
            cv2.imshow('Video', frame1)
                    
    cv2.imshow('Video', frame1)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
vedio.release()
cv2.destroyAllWindows()