# https://www.kevsrobots.com/blog/cvzone.html converted program to use a PI Camera rather than a webcam
#hand1.py


import cv2
from cvzone.HandTrackingModule import HandDetector
from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)})


print(config)
picam2.configure(config)
picam2.start()

detector = HandDetector(detectionCon=0.5, maxHands=2)

while True:
	imgRGBA = picam2.capture_array()  # imgRGBA is 4 channels of alpha and RGB
	img = cv2.cvtColor(imgRGBA, cv2.COLOR_RGBA2RGB) # get rid of the alpha channel
	total_fingers = 0
	
	hands, img = detector.findHands(img)
	
	gesture = ""
	
	if hands:
		
		hand1 = hands[0]
		lmlistq = hand1["lmList"]  
		bbox1 = hand1["bbox"]
		centrepoint1 = hand1["center"]
		handType1 = hand1["type"]
		
		fingers1 = detector.fingersUp(hand1)
		
		if fingers1 == [0, 0, 0, 1, 1]:
			gesture = "peace"
		elif fingers1 == [0, 0, 0, 0, 1]:
			gesture = "thumbsup"
		elif  fingers1 == [0, 1, 1,1, 1]:
			gesture = "four"
		#hand2
		hand2 = hands[0]
		lmlistq = hand2["lmList"]
		bbox2 = hand2["bbox"]
		centrepoint2 = hand2["center"]
		handType2 = hand2["type"]
		fingers2 = detector.fingersUp(hand2)
		total_fingers += sum(fingers2)
		
	finger_count = str(total_fingers)
	cv2.putText(img, gesture, (410, 215), cv2.FONT_HERSHEY_PLAIN,4, (237, 34, 13), 6)
	cv2.putText(img, finger_count, (410, 215), cv2.FONT_HERSHEY_PLAIN,4, (237,34,13),6)
	cv2.imshow("Image", img)
	cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
