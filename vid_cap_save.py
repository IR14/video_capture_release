import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'WIDX') # Define the codec and create VideoWriter object
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
ret = cap.set(3,1000) # (3,x) - width ~ (4,y) - height, so 640x480 by default
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame) # write the frame in grayscale
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()