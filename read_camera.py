import cv2
out = cv2.imread("unnamed.png",0)
cv2.imshow("output",out)
cv2.imwrite("output.png",out)
cv2.waitKey(0)
print(out)