import cv2

img = cv2.imread('izone.jpg')
img2 = cv2.resize(img, (1024, 768))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_outline1 = cv2.Canny(img, 150, 200)
img_outline2 = cv2.Canny(img, 100, 150)
img_outline3 = cv2.Canny(img, 50, 100)

cv2.imshow('IZONE', img)
cv2.imshow('IZONE BUT SMALLER', img2)
cv2.imshow('IZONE BUT GRAY(NOT GREY)', img_gray)

cv2.imshow('IZONE BUT OUTLINED SLIGHTLY', img_outline1)
cv2.imshow('IZONE BUT OUTLINED NORMALLY', img_outline2)
cv2.imshow('IZONE BUT OUTLINED EXCESSIVELY', img_outline3)

while True:
    if cv2.waitKey() ==13:
        break

cv2.imwrite('IZONE_GRAY.jpg', img_gray)

cv2.destroyAllWindows()
