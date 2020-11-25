import cv2
import numpy

def hello(x):
	print("")

cap = cv2.VideoCapture(0)
IDK = cv2.namedWindow("IDK what to call thissssssss")

cv2.createTrackbar("upper_hue","IDK what to call thissssssss",110,180,hello)
cv2.createTrackbar("upper_saturation","IDK what to call thissssssss",255, 255, hello)
cv2.createTrackbar("upper_value","IDK what to call thissssssss",255, 255, hello)
cv2.createTrackbar("lower_hue","IDK what to call thissssssss",68,180, hello)
cv2.createTrackbar("lower_saturation","IDK what to call thissssssss",55, 255, hello)
cv2.createTrackbar("lower_value","IDK what to call thissssssss",54, 255, hello)


while(True):
	cv2.waitKey(1000)
	ret,init_frame = cap.read()
	if(ret):
		break

while(True):
	ret,frame = cap.read()
	inspect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	upper_hue = cv2.getTrackbarPos("upper_hue", "IDK what to call thissssssss")
	upper_saturation = cv2.getTrackbarPos("upper_saturation", "IDK what to call thissssssss")
	upper_value = cv2.getTrackbarPos("upper_value", "IDK what to call thissssssss")
	lower_value = cv2.getTrackbarPos("lower_value","IDK what to call thissssssss")
	lower_hue = cv2.getTrackbarPos("lower_hue","IDK what to call thissssssss")
	lower_saturation = cv2.getTrackbarPos("lower_saturation","IDK what to call thissssssss")
	
	kernel = numpy.ones((11,11),numpy.uint8)

	upper_hsv = numpy.array([upper_hue,upper_saturation,upper_value])
	lower_hsv = numpy.array([lower_hue,lower_saturation,lower_value])

	mask = cv2.inRange(inspect, lower_hsv, upper_hsv)
	mask = cv2.medianBlur(mask,3)
	mask_inv = 255-mask 
	mask = cv2.dilate(mask,kernel,5)
	
	#The mixing of frames in a combination to achieve the required frame
	b = frame[:,:,0]
	g = frame[:,:,1]
	r = frame[:,:,2]
	b = cv2.bitwise_and(mask_inv, b)
	g = cv2.bitwise_and(mask_inv, g)
	r = cv2.bitwise_and(mask_inv, r)
	frame_inv = cv2.merge((b,g,r))

	b = init_frame[:,:,0]
	g = init_frame[:,:,1]
	r = init_frame[:,:,2]
	b = cv2.bitwise_and(b,mask)
	g = cv2.bitwise_and(g,mask)
	r = cv2.bitwise_and(r,mask)
	blanket_area = cv2.merge((b,g,r))

	final = cv2.bitwise_or(frame_inv, blanket_area)

	cv2.imshow("Harry's Cloak",final)

	if(cv2.waitKey(3) == ord('q')):
		break;

cv2.destroyAllWindows()
cap.release()
