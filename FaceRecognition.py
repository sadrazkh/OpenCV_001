import cv2
import face_recognition

shajarian01 = "./Images/download.jpg"
shajarian02 = "./Images/download (1).jpg"
shajarian03 = "./Images/download (2).jpg"

imgShajarian01 = face_recognition.load_image_file(shajarian01)
imgShajarian02 = face_recognition.load_image_file(shajarian02)
imgShajarian03 = face_recognition.load_image_file(shajarian03)

shajarian01_face_loc = face_recognition.face_locations(imgShajarian01)
shajarian02_face_loc = face_recognition.face_locations(imgShajarian02)
shajarian03_face_loc = face_recognition.face_locations(imgShajarian03)


for face in shajarian01_face_loc:
    face_rec = cv2.rectangle(imgShajarian01, (face[3], face[0]),
                             (face[1], face[2]), (155, 0, 255), 3)

for face in shajarian02_face_loc:
    face_rec = cv2.rectangle(imgShajarian02, (face[3], face[0]),
                             (face[1], face[2]), (155, 0, 255), 3)

for face in shajarian03_face_loc:
    face_rec = cv2.rectangle(imgShajarian03, (face[3], face[0]),
                             (face[1], face[2]), (155, 0, 255), 3)



shajarian01_face_code = face_recognition.face_encodings(imgShajarian01)
shajarian02_face_code = face_recognition.face_encodings(imgShajarian02)
shajarian03_face_code = face_recognition.face_encodings(imgShajarian03)



imgShajarian01 = cv2.cvtColor(imgShajarian01, cv2.COLOR_RGB2BGR)
imgShajarian02 = cv2.cvtColor(imgShajarian02, cv2.COLOR_RGB2BGR)
imgShajarian03 = cv2.cvtColor(imgShajarian03, cv2.COLOR_RGB2BGR)


isSame = face_recognition.compare_faces(shajarian01_face_code, shajarian02_face_code[0])
#isSame2 = face_recognition.compare_faces(shajarian01_face_code, shajarian03_face_code[0])

dist = face_recognition.face_distance(shajarian01_face_code, shajarian02_face_code[0])
#dist2 = face_recognition.face_distance(shajarian01_face_code, shajarian03_face_code[0])

print(isSame, dist)
#print(isSame2, dist2)

cv2.imshow("1", imgShajarian01)
cv2.imshow("2", imgShajarian02)
cv2.imshow("3", imgShajarian03)

cv2.waitKey()