import cv2

from handchecker import HandChecker
from palm import Palm
from letterfinder import LetterFinder
import mediapipe as mp
import datetime

hand=input() #Рука, выбираемая пользователем(R - правая, L - левая)
red = (0,0,255) #Кортеж RGB для красного цвета
blue = (255, 0, 0) #Кортеж RGB для синего цвета
word = '' #Слово
letter = '' #Буква
meaning = False #Значение, которое включает функции в определённый временной промежуток

camera = cv2.VideoCapture(0) #Видео с камеры

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

lf = LetterFinder() #Класс LetterFinder
hc = HandChecker(hand) #Класс HandChecker

while True:
    good, img = camera.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image_height, image_width, _ = img.shape

    millisec = datetime.datetime.now().time().microsecond // 1000 #Миллисекунды
    sec = datetime.datetime.now().time().second #Секунды
    if sec % 5 == 0:
        border = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=red)
        if 200 < millisec < 245:
            meaning = True
    else:
        border = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=blue)
        meaning = False

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(border, hand_landmarks, mpHands.HAND_CONNECTIONS)

            if meaning == True:
                rot = hc.checkHandRotate(hand_landmarks.landmark)
                fin = hc.checkHandFingers(hand_landmarks.landmark)

                next = lf.getLetter(hand, rot, fin, hand_landmarks.landmark)
                if next != '':
                    word += next
                print(word)
                meaning = False


    cv2.imshow("Result", border)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()


