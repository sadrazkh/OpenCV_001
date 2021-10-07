import cv2

img = cv2.imread("Images/109666.jpg", 1)
cv2.imshow("Show Test", img)
cv2.waitKey(6000)
cv2.imwrite("Test New File.png", img)
cv2.destroyWindows()