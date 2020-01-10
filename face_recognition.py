import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
        ret, frame=cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,4)
        for (x,y,w,h) in faces:
                if(w>0):
                        cv2.rectangle(frame,(x,y), (x+w, y+h), (255,0,0), 1)
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(frame, "Tanmay", (x+int(w/4),y), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('output',frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
                break
                
cap.release()
cv2.destroyAllWindows()
