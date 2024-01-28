import cv2

out = cv2.imread("output.png",0)
colour = cv2.cvtColor(out,cv2.COLOR_GRAY2BGR)

cv2.imshow("output",colour)
cv2.imwrite("output.png",colour)
cv2.waitKey(0)
