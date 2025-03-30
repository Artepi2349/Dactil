from palm import Palm

class HandChecker:
    """
    Здесь собраны функции для распознавания положения ладони в пространстве
    :param h: Рука, выбранная пользователем
    """

    sel_hand = '' #Выбранная рука
    rotate = '' #Поворот руки в пространстве
    fingers = '' #Куда повёрнуты пальцы

    def __init__(self, h):
        self.sel_hand = h

    def checkHandFingers(self, landmark):
        """
        Функция для определения поворота пальцев
        :param landmark: Массив координат точек на ладони
        """

        if self.__fingersUp(landmark):
            fingers = 'Up'
        if self.__fingersDown(landmark):
            fingers = 'Down'
        if self.__fingersMiddle(landmark):
            fingers = 'Middle'
        return fingers

    def checkHandRotate(self, landmark):
        """
        Функция для определения поворота ладони в пространстве
        :param landmark: Массив координат точек на ладони
        """

        if self.__rotateBackR(landmark) or self.__rotateBackL(landmark):
            rotate = 'Back'
        if self.__rotateFrontR(landmark) or self.__rotateFrontL(landmark):
            rotate = 'Front'
        if self.__rotateMiddleR(landmark) or self.__rotateMiddleL(landmark):
            rotate = 'Middle'
        return rotate

    # Private functions
    def __fingersUp(self,landmark) -> bool:
        return ((landmark[Palm.MIDDLE_FINGER_MCP].y / landmark[Palm.THUMB_CMC].y < 0.85) and
                (0.9 < landmark[Palm.MIDDLE_FINGER_MCP].x / landmark[Palm.WRIST].x < 1.1))
    def __fingersDown(self, landmark) -> bool:
        return ((landmark[Palm.MIDDLE_FINGER_MCP].y / landmark[Palm.THUMB_CMC].y > 1.2))
    def __fingersMiddle(self, landmark) -> bool:
        return ((0.85 < landmark[Palm.MIDDLE_FINGER_MCP].y / landmark[Palm.THUMB_CMC].y < 1.2) or
                (landmark[Palm.MIDDLE_FINGER_MCP].x / landmark[Palm.WRIST].x > 1.1 or
                 landmark[Palm.MIDDLE_FINGER_MCP].x / landmark[Palm.WRIST].x < 0.9))

    def __rotateFrontR(self,landmark) -> bool:
        if self.__fingersDown(landmark):
            return self.sel_hand == 'R' and landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x > 1.1
        elif self.__fingersUp(landmark):
            return (self.sel_hand == 'R' and
                    (landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 0.9 < \
                     landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y < 1.1))
        else:
            if landmark[Palm.MIDDLE_FINGER_MCP].x > landmark[Palm.WRIST].x:
                return self.sel_hand == 'R' and landmark[Palm.INDEX_FINGER_MCP].y /  \
                       landmark[Palm.PINKY_MCP].y < 0.9 < landmark[Palm.INDEX_FINGER_MCP].x /  \
                       landmark[Palm.PINKY_MCP].x < 1.1
            else:
                return self.sel_hand == 'R' and  0.9 < landmark[Palm.INDEX_FINGER_MCP].x / \
                       landmark[Palm.PINKY_MCP].x < 1.1 < landmark[Palm.INDEX_FINGER_MCP].y / \
                       landmark[Palm.PINKY_MCP].y
    def __rotateBackR(self,landmark) -> bool:
        if self.__fingersDown(landmark):
            return self.sel_hand == 'R' and landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x \
                   < 0.9
        elif self.__fingersUp(landmark):
            return (self.sel_hand =='R' and
                    (0.9 < landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y < 1.1 < \
                     landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x))
        else:
            if landmark[Palm.MIDDLE_FINGER_MCP].x > landmark[Palm.WRIST].x:
                return self.sel_hand == 'R' and  0.9 < landmark[Palm.INDEX_FINGER_MCP].x / \
                       landmark[Palm.PINKY_MCP].x < 1.1 < landmark[Palm.INDEX_FINGER_MCP].y / \
                       landmark[Palm.PINKY_MCP].y
            else:
                return self.sel_hand == 'R' and landmark[Palm.INDEX_FINGER_MCP].y / \
                       landmark[Palm.PINKY_MCP].y < 0.9 < landmark[Palm.INDEX_FINGER_MCP].x / \
                       landmark[Palm.PINKY_MCP].x < 1.1
    def __rotateMiddleR(self,landmark) -> bool:
        return (self.sel_hand == 'R' and 0.9 < landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 1.1 and
                0.9 < landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y < 1.1)

    def __rotateFrontL(self,landmark) -> bool:
        if self.__fingersDown(landmark):
            return self.sel_hand == 'L' and landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 0.9
        elif self.__fingersUp(landmark):
            return (self.sel_hand == 'L' and
                    (0.9 < landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y < 1.1 < landmark[
                        Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x))
        else:
            if landmark[Palm.MIDDLE_FINGER_MCP].x > landmark[Palm.WRIST].x:
                return self.sel_hand == 'L' and 0.9 < landmark[Palm.INDEX_FINGER_MCP].x / landmark[
                    Palm.PINKY_MCP].x < 1.1 < landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y
            else:
                return self.sel_hand == 'L' and landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y < 0.9 < \
                    landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 1.1
    def __rotateBackL(self,landmark) -> bool:
        if self.__fingersDown(landmark):
            return self.sel_hand == 'L' and landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x > 1.1
        elif self.__fingersUp(landmark):
            return (self.sel_hand == 'L' and
                    (landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 0.9 < landmark[
                        Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y < 1.1))
        else:
            if landmark[Palm.MIDDLE_FINGER_MCP].x > landmark[Palm.WRIST].x:
                return self.sel_hand == 'L' and landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y < 0.9 < \
                    landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 1.1
            else:
                return self.sel_hand == 'L' and 0.9 < landmark[Palm.INDEX_FINGER_MCP].x / landmark[
                    Palm.PINKY_MCP].x < 1.1 < landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y
    def __rotateMiddleL(self,landmark) -> bool:
        return (self.sel_hand=='L' and 0.9 < landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 1.1 and
                0.9 < landmark[Palm.INDEX_FINGER_MCP].y / landmark[Palm.PINKY_MCP].y < 1.1)

if __name__ == '__main__':
    print('You should not run this file. Call main.py instead')