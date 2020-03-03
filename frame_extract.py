import cv2

video_name = input()

#Opens the video file, we can set video_name=0 for Camera
cap = cv2.VideoCapture(video_name)

#we are considering frames per sec as 30
fps=30

i=0
while(cap.isOpened()):
    #since we are extracting frames at every 0.2 sec
    frame_no= int(i*fps*0.2)
    cap.set(1,frame_no)
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('frame'+str(i)+'.jpg',frame)
    i+=1
    
cap.release()
cv2.destroyAllWindows()
