import cv2

from handchecker import HandChecker
from palm import Palm
from letterfinder import LetterFinder
import mediapipe as mp
import datetime

hand=input()
i=1
red = (0,0,255)
blue = (255, 0, 0)
word = ''
letter = ''
meaning = 0

#letterFinder = LetterFinder
#handChecker = HandChecker

camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

lf = LetterFinder()
hc = HandChecker(hand)

while True:
    good, img = camera.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image_height, image_width, _ = img.shape

    results = hands.process(img)

    millisec = datetime.datetime.now().time().microsecond // 1000
    sec = datetime.datetime.now().time().second
    if sec % 5 == 0:
        border = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=red)
        if 200 < millisec < 275:
            meaning = 1
    else:
        border = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=blue)
        meaning = 0

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(border, hand_landmarks, mpHands.HAND_CONNECTIONS)

            hc.checkHand(hand_landmarks.landmark)

            if meaning == 1:
                word += lf.getLetter(hand_landmarks.landmark)
                print(word)
                meaning = 0

    cv2.imshow("Result", border)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()


