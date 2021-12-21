import cv2

#xml 분류기 파일 로그
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

#Gray스케일 이미지로 변환
img = cv2.imread('avengers.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#이미지에서 얼굴 검출
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#얼굴 위치 좌표 가져오기
for(x, y, w, h) in faces:
    #원본 이미지에 얼굴 위치 표시
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    #roi : 관심영역 -> 각 얼굴
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]
    

    eyes = eye_cascade.detectMultiScale(roi_gray)

    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()