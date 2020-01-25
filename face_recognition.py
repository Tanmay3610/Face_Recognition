import cv2
import numpy as np

smile = cv2.CascadeClassifier("haarcascade_smile.xml")
faces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
	res,frame = cap.read()
	if res == True:
		frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		face = faces.detectMultiScale(frame_gray,1.3,5)
		
		for (x,y,w,h) in face:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)
			ros_gray = frame_gray[y:y+h, x:x+w]
			ros_color = frame[y:y+h, x:x+w]
			smiles = smile.detectMultiScale(ros_gray,1.3,25)
			for(sx,sy,sw,sh) in smiles:
				cv2.rectangle(ros_color,(sx,sy),(sx+sw,sy+sh),(255,0,0),1)
		cv2.imshow("frame",frame)
			
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
cap.release()
cv2.destroyAllWindows()
