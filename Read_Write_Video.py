import cv2

cap = cv2.VideoCapture("Video/test001.mp4")
# cap = cv2.VideoCapture(0)
# while cap.isOpened()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Test Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
        break

cap.release()
cv2.destroyAllWindows()
