import cv2

cap = cv2.VideoCapture("Video/test001.mp4")
# cap = cv2.VideoCapture(0)
# while cap.isOpened()
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

out = cv2.VideoWriter('TestWrite.mp4', fourcc, 20.0, (1920,1080))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('Test Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
