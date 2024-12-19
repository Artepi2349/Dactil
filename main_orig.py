import cv2
import mediapipe as mp
import datetime


hand=input()
rotate=''
fingers = ''
i=1
red = [0,0,255]
blue = [255, 0, 0]
word = ''
letter = ''
meaning = 0

camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



while True:
    good, img = camera.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image_height, image_width, _ = img.shape

    results = hands.process(img)

    microsec = datetime.datetime.now().time().microsecond
    sec = datetime.datetime.now().time().second
    if sec % 5 == 0:
        border = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=red)
        if 200000 < microsec < 275000:
            meaning = 1
    else:
        border = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=blue)
        meaning = 0



    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(border, hand_landmarks, mpHands.HAND_CONNECTIONS)


            x0 = hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x
            x1 = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_CMC].x
            x2 = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_MCP].x
            x3 = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_IP].x
            x4 = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x
            x5 = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_MCP].x
            x6 = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_PIP].x
            x7 = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].x
            x8 = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x
            x9 = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP].x
            x10 = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_PIP].x
            x11 = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].x
            x12 = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].x
            x13 = hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_MCP].x
            x14 = hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_PIP].x
            x15 = hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_DIP].x
            x16 = hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_TIP].x
            x17 = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_MCP].x
            x18 = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_PIP].x
            x19 = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_DIP].x
            x20 = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].x

            y0 = hand_landmarks.landmark[mpHands.HandLandmark.WRIST].y
            y1 = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_CMC].y
            y2 = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_MCP].y
            y3 = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_IP].y
            y4 = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].y
            y5 = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_MCP].y
            y6 = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_PIP].y
            y7 = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y
            y8 = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y
            y9 = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP].y
            y10 = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_PIP].y
            y11 = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y
            y12 = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y
            y13 = hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_MCP].y
            y14 = hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_PIP].y
            y15 = hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_DIP].y
            y16 = hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y
            y17 = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_MCP].y
            y18 = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_PIP].y
            y19 = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_DIP].y
            y20 = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y


            def print_msg():
                if fingers == 'up' and rotate == 'front':
                    print('Пальцы вверху, ладонь передом')
                if fingers == 'up' and rotate == 'back':
                    print('Пальцы вверху, ладонь тылом')
                if fingers == 'up' and rotate == 'middle':
                    print('Пальцы вверху, ладонь посередине')

                if fingers == 'down' and rotate == 'front':
                    print('Пальцы снизу, ладонь передом')
                if fingers == 'down' and rotate == 'back':
                    print('Пальцы снизу, ладонь тылом')
                if fingers == 'down' and rotate == 'middle':
                    print('Пальцы снизу, ладонь посередине')

                if fingers == 'middle' and rotate == 'front':
                    print('Пальцы посередине, ладонь передом')
                if fingers == 'middle' and rotate == 'back':
                    print('Пальцы посередине, ладонь тылом')
                if fingers == 'middle' and rotate == 'middle':
                    print('Пальцы посередине, ладонь посередине')


            def RFingersUp():
                global rotate
                if x4 / x20 > 1.2:
                    if rotate != 'back':
                        rotate = 'back'
                        print_msg()

                elif x4 / x20 < 0.93:
                    if rotate != 'front':
                        rotate = 'front'
                        print_msg()

                elif 0.93<x4/x20<1.2 and y20<y4:
                    if rotate != 'middle':
                        rotate = 'middle'
                        print_msg()

            def RFingersDown():
                global rotate
                if x4 / x20 < 0.93:
                    if rotate != 'back':
                        rotate = 'back'
                        print_msg()
                elif x4 / x20 > 1.2:
                    if rotate != 'front':
                        rotate = 'front'
                        print_msg()

                else:
                    if rotate != 'middle':
                        rotate = 'middle'
                        print_msg()


            def LFingersUp():
                global rotate
                if x4 / x20 < 0.93 :
                    if rotate != 'back':
                        rotate = 'back'
                        print_msg()

                elif x4 / x20 > 1.2:
                    if rotate != 'front':
                        rotate = 'front'
                        print_msg()

                else:
                    if rotate != 'middle':
                        rotate = 'middle'
                        print_msg()


            def LFingersDown():
                global rotate
                if x4 / x20 < 0.93:
                    if rotate != 'back':
                        rotate = 'back'
                        print_msg()

                elif x4 / x20 >1.2:
                    if rotate != 'front':
                        rotate = 'front'
                        print_msg()

                else:
                    if rotate != 'middle':
                        rotate = 'middle'
                        print_msg()


            def FingersMiddle():
                global rotate
                if y4 / y20 < 0.93:
                    if rotate != 'back':
                        rotate = 'back'
                        print_msg()

                elif y4 / y20 > 1.2:
                    if rotate != 'front':
                        rotate = 'front'
                        print_msg()

                else:
                    if rotate != 'middle':
                        rotate = 'middle'
                        print_msg()



            if hand == 'R':

                if y0 / y12 > 1.2:
                    if fingers != 'up':
                        fingers = 'up'
                        print_msg()

                elif y0 / y12 < 0.8:
                    if fingers != 'down':
                        fingers = 'down'
                        print_msg()

                else:
                    if fingers != 'middle':
                        fingers = 'middle'
                        print_msg()


                if fingers=='up':
                    RFingersUp()
                elif fingers=='down':
                    RFingersDown()
                else:
                    FingersMiddle()
            elif hand == 'L':

                if y0 / y12 > 1.5:
                    if fingers != 'up':
                        fingers = 'up'
                        print_msg()

                elif y0 / y12 < 0.7:
                    if fingers != 'down':
                        fingers = 'down'
                        print_msg()

                else:
                    if fingers != 'middle':
                        fingers = 'middle'
                        print_msg()


                if fingers == 'up':
                    LFingersUp()
                elif fingers == 'down':
                    LFingersDown()
                else:
                    FingersMiddle()
            else:
                print('Значение введено неправильно')


            def check_а():
                pass
            def check_б():
                pass
            def check_вR():
                    if (y8 < y4 and y12 < y4 and y16 < y4 and y20 < y4) and (x4 < x5):
                        #print('В')
                        global letter
                        letter = 'В'
            def check_вL():
                    if (y8 < y4 and y12 < y4 and y16 < y4 and y20 < y4) and (x4 > x5):
                        #print('В')
                        global letter
                        letter = 'В'
            def check_г():
                pass
            def check_д():
                pass
            def check_е():
                pass
            def check_ё():
                pass
            def check_ж():
                pass
            def check_з():
                pass
            def check_и():
                if (y16 < y4 and y20 < y4) and (0.8 < y4/y8 <1.2) and (0.8 < y4/y12 <1.2):
                    #print('И')
                    global letter
                    letter = 'И'
            def check_й():
                pass
            def check_к():
                pass
            def check_л():
                pass
            def check_м():
                pass
            def check_н():
                if (y8 < y4 and y12 < y4 and y20 < y4) and (0.8 < y4/y15 <1.2):
                    #print('Н')
                    global letter
                    letter = 'Н'
            def check_о():
                pass
            def check_п():
                pass
            def check_р():
                if (y8 < y4 and y16 < y4 and y20 < y4) and (0.8 < y4/y11 < 1.2):
                    #print('Р')
                    global letter
                    letter = 'Р'
            def check_с():
                pass
            def check_т():
                pass
            def check_у():
                pass
            def check_ф():
                pass
            def check_х():
                pass
            def check_ц():
                pass
            def check_ч():
                pass
            def check_ш():
                if (y8 < y4 and y12 < y4 and y16 < y4) and 0.8 < y4/y19< 1.2:
                    #print('Ш')
                    global letter
                    letter = 'Ш'
            def check_щ():
                pass
            def check_ъ():
                pass
            def check_ы():
                if (y8 < y4 and y20 < y4) and (0.8 < y4 / y15 < 1.2) and (0.8 < y4/y11 < 1.2):
                    #print('Ы')
                    global letter
                    letter = 'Ы'
            def check_ь():
                pass
            def check_э():
                pass
            def check_ю():
                pass
            def check_я():
                pass

            if fingers == 'up' and rotate == 'front' and hand == 'R':
                check_и()
                check_н()
                check_вR()
                check_р()
                check_ы()
                check_ш()
            #В - ладонь вперёд(rotate == 'front'), пальцы вверх(fingers == 'up')



            if meaning == 1:
                word += letter
                print(word)
                meaning = 0

            print(x5/x17)
            #R
            # <0,8 - фронт
            #>1.25 - тыл

    cv2.imshow("Result", border)


    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()


