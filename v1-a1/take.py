import cv2

def take():
        cap = cv2.VideoCapture(0)
        #cap.set(3,1920) #setting width
        #cap.set(4,1080) #setting high

        if cap.isOpened():
            _,frame = cap.read()
            frame = cv2.flip(frame, 1)
            cap.release() #releasing camera immediately after capturing picture
            if _ and frame is not None:
                cv2.imwrite('img.jpg', frame)

