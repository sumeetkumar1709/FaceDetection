import cv2

vid = cv2.VideoCapture(0)
vid.set(3,640) # width
vid.set(4,480) # height
vid.set(10,100) # brightness
while True:
    success, img = vid.read()
    faceCascade = cv2.CascadeClassifier("resource/haarcascade_frontalface_default.xml")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(img_gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img,'Human',(x-10,y-20),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),1)
    cv2.imshow("VIDEO",img)

    # press q to close video window
    if cv2.waitKey(4) & 0xFF==ord('q'):
        break
