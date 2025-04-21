import cv2
import os
from handchecker import HandChecker
from letterfinder import LetterFinder
import mediapipe as mp
import datetime
import gtts
from playsound import playsound

print('Выберите руку, которой будете показывать жесты(R - правая, L - левая)')

hand=input() #Рука, выбираемая пользователем(R - правая, L - левая)

print('Выберите режим работы(T - текст, W - слово)')

mode = input()
red = (0,0,255) #Кортеж RGB для красного цвета
blue = (255, 0, 0) #Кортеж RGB для синего цвета
text = '' #Текст
word = '' #Слово
letter = '' #Буква
meaning = False #Значение, которое включает функции в определённый временной промежуток
breakMean = 0

camera = cv2.VideoCapture(0) #Видео с камеры

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

lf = LetterFinder() #Класс LetterFinder
hc = HandChecker(hand) #Класс HandChecker

start_sec = datetime.datetime.now().time().second

clear = lambda: os.system('cls')

while True:
    if (hand == 'R' or hand == 'L') and (mode == 'T' or mode == 'W'):
        good, img = camera.read()
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image_height, image_width, _ = img.shape

        millisec = datetime.datetime.now().time().microsecond // 1000 #Миллисекунды
        sec = datetime.datetime.now().time().second #Секунды
        if abs(start_sec - sec) % 5 == 0:
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

                    clear()

                    fin = hc.checkHandFingers(hand_landmarks.landmark)
                    rot = hc.checkHandRotate(hand_landmarks.landmark)
                    print(rot)
                    print(fin)

                    next = lf.getLetter(hand, rot, fin, hand_landmarks.landmark)
                    if next == 'break':
                        breakMean = 1
                        print('Не делай так')
                    elif next == ' ':
                        if mode == 'T':
                            word += next
                            text += word
                            print(text)
                            word = ''
                            print('Пробел')
                        else:
                            print('Не тот режим работы')
                    elif next == 'stop':
                        if mode == 'W':
                            print(word)
                            tts = gtts.gTTS(word, lang='ru')
                            tts.save("word2.mp3")
                            playsound("word2.mp3")
                            breakMean = 1
                        else:
                            text += word
                            print(text)
                            tts = gtts.gTTS(text, lang='ru')
                            tts.save("text1.mp3")
                            playsound("text1.mp3")
                            breakMean = 1
                    elif next != '':
                        word += next
                        print(word)
                    meaning = False

        if breakMean == 1:
            break
        cv2.imshow("Result", border)

        if cv2.waitKey(1) == 27:
            break
    else:
        print('Ошибка в введённых данных, попробуйте ещё раз')
        break

camera.release()
cv2.destroyAllWindows()


