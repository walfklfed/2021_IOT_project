import cv2

cap = cv2.VideoCapture('output.avi')

if not cap.isOpened():
    print('Camera open failed')
    exit()

# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('output.avi', fourcc, 60, (640, 480))

# 사진 찍기
# ret, frame = cap.read()
# cv2.imshow('frame', frame)
# cv2.imwrite('output.jpg', frame)
# cv2.waitKey(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    # out.write(frame)

    if cv2.waitKey(10) == 13:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()