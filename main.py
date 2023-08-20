import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key,Controller

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 420)

detector = HandDetector(detectionCon=0.7, maxHands=1)
keyboard = Controller()
while True:
    _, image = cap.read()
    img = cv2.flip(image,1)
    hands, img = detector.findHands(img)
    if hands:
        fingers = detector.fingersUp(hands[0])
        if fingers == [0,0,0,0,0]:
            keyboard.release(Key.down)
            print("fingers down")
        elif fingers == [1,1,1,1,1]:
            keyboard.press(Key.space)
            keyboard.release(Key.down)
            print("fingers up")
        elif fingers == [0,1,0,0,0]:
            keyboard.press(Key.down)
            keyboard.release(Key.space)
            print("one finger up")
    cv2.imshow("Fingers by Keith", img)
    if cv2.waitKey(1) == ord("q"):
        break