#!/usr/bin/python3

from palm import Palm

class LetterFinder:
    """
    Здесь собраны фунции для определения буквы, которую показывает пользователь
    """

    def __init__(self):
        pass

    def getLetter(self, hand, rotate, fingers, landmark) -> str:


        """
        Функуия для выбора буквы
        :param hand: Рука, выбранная пользователем
        :param rotate: Положение ладони в пространстве
        :param fingers: Поворот пальцев
        :param landnmark: Массив координат точек на ладони
        """
        if rotate == 'Front' and fingers == 'Up':
            if self.__isLetter_Ы(landmark):
                return 'Ы'
            if self.__isLetter_И(landmark):
                return 'И'
            if self.__isLetter_Н(landmark):
                return 'Н'
            if self.__isLetter_Ш(landmark):
                return 'Ш'
            if self.__isLetter_Р( landmark):
                return 'Р'
            if hand == 'R':
                if self.__isLetter_ВR( landmark):
                    return 'В'
            if hand == 'L':
                if self.__isLetter_ВL(landmark):
                    return 'В'
        if rotate == 'Front' and fingers == 'Middle':
            if hand == 'R':
                if self.__isLetter_АR(landmark):
                    return 'А'
            if hand == 'L':
                if self.__isLetter_AL(landmark):
                    return 'А'
        if rotate == 'Front' and fingers == 'Down':
            if hand == 'R':
                if self.__isLetter_ГR(landmark):
                    return 'Г'
            if hand == 'L':
                if self.__isLetter_ГL(landmark):
                    return 'Г'

        if rotate == 'Middle' and fingers == 'Up':
            pass
        if rotate == 'Middle' and fingers == 'Middle':
            if hand == 'R':
                if self.__isLetter_СR(landmark):
                    return 'С'
                if self.__isLetter_ЕR(landmark):
                    return 'Е'
                if self.__isLetter_ЖR(landmark):
                    return 'Ж'
                if self.__isLetter_ФR(landmark):
                    return 'Ф'
            if hand == 'L':
                if self.__isLetter_СL(landmark):
                    return 'С'
                if self.__isLetter_ЕL(landmark):
                    return 'Е'
                if self.__isLetter_ЖL(landmark):
                    return 'Ж'
                if self.__isLetter_ФL(landmark):
                    return 'Ф'
        if rotate == 'Middle' and fingers == 'Down':
            pass

        if rotate == 'Back' and fingers == 'Up':
            pass
        if rotate == 'Back' and fingers == 'Middle':
            pass
        if rotate == 'Back' and fingers == 'Down':
            if hand == 'R':
                if self.__isLetter_ЛR(landmark):
                    return 'Л'
                if self.__isLetter_ПR(landmark):
                    return 'П'
                if self.__isLetter_МR(landmark):
                    return 'М'
                if self.__isLetter_ТR(landmark):
                    return 'Т'
            if hand == 'L':
                if self.__isLetter_ЛL(landmark):
                    return 'Л'
                if self.__isLetter_ПL(landmark):
                    return 'П'
                if self.__isLetter_МL(landmark):
                    return 'М'
                if self.__isLetter_ТL(landmark):
                    return 'Т'

        return ''

    # Private functions
    def __isLetter_АR(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.RING_FINGER_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.PINKY_TIP].y) and
                (landmark[Palm.THUMB_TIP].y < landmark[Palm.INDEX_FINGER_DIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_DIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.RING_FINGER_DIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.PINKY_DIP].y) and
                (landmark[Palm.INDEX_FINGER_PIP].x > landmark[Palm.INDEX_FINGER_TIP].x and
                 landmark[Palm.MIDDLE_FINGER_PIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.RING_FINGER_PIP].x > landmark[Palm.RING_FINGER_TIP].x and
                 landmark[Palm.PINKY_PIP].x > landmark[Palm.PINKY_TIP].x) and
                (landmark[Palm.WRIST].x < landmark[Palm.THUMB_TIP].x))

    def __isLetter_AL(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.RING_FINGER_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.PINKY_TIP].y) and
                (landmark[Palm.THUMB_TIP].y < landmark[Palm.INDEX_FINGER_DIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_DIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.RING_FINGER_DIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.PINKY_DIP].y) and
                (landmark[Palm.INDEX_FINGER_PIP].x < landmark[Palm.INDEX_FINGER_TIP].x and
                 landmark[Palm.MIDDLE_FINGER_PIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.RING_FINGER_PIP].x < landmark[Palm.RING_FINGER_TIP].x and
                 landmark[Palm.PINKY_PIP].x < landmark[Palm.PINKY_TIP].x) and
                (landmark[Palm.WRIST].x > landmark[Palm.THUMB_TIP].x))
    def __isLetter_Б(self, landmark) -> bool:
        pass
    def __isLetter_ВR(self, landmark) -> bool:
        return (landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.PINKY_TIP].y < landmark[Palm.THUMB_TIP].y) and \
                (landmark[Palm.THUMB_TIP].x < landmark[Palm.INDEX_FINGER_TIP].x)
    def __isLetter_ВL(self, landmark) -> bool:
        return (landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.PINKY_TIP].y < landmark[Palm.THUMB_TIP].y) and \
                (landmark[Palm.THUMB_TIP].x > landmark[Palm.INDEX_FINGER_TIP].x)
    def __isLetter_ГR(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.MIDDLE_FINGER_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.RING_FINGER_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.PINKY_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.THUMB_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y) and
               (landmark[Palm.WRIST].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                landmark[Palm.WRIST].y < landmark[Palm.RING_FINGER_TIP].y and
                landmark[Palm.WRIST].y < landmark[Palm.PINKY_TIP].y) and
               (landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_PIP].y and
                landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.RING_FINGER_PIP].y and
                landmark[Palm.PINKY_TIP].y < landmark[Palm.PINKY_PIP].y) and
               (landmark[Palm.THUMB_TIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x))
    def __isLetter_ГL(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.RING_FINGER_TIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.PINKY_TIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.THUMB_TIP].y and
                 landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.WRIST].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.WRIST].y < landmark[Palm.RING_FINGER_TIP].y and
                 landmark[Palm.WRIST].y < landmark[Palm.PINKY_TIP].y) and
                (landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_PIP].y and
                 landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.RING_FINGER_PIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.PINKY_PIP].y) and
                (landmark[Palm.THUMB_TIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x))
    def __isLetter_Д(self, landmark) -> bool:
        pass

    def __isLetter_ЕR(self, landmark) -> bool:
        return (landmark[Palm.THUMB_TIP].x > landmark[Palm.THUMB_CMC].x and
                landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.INDEX_FINGER_MCP].x and
                landmark[Palm.MIDDLE_FINGER_TIP].x > landmark[Palm.MIDDLE_FINGER_MCP].x and
                landmark[Palm.RING_FINGER_TIP].x > landmark[Palm.RING_FINGER_MCP].x and
                landmark[Palm.PINKY_TIP].x > landmark[Palm.PINKY_MCP].x and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.INDEX_FINGER_MCP].y and
                landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.MIDDLE_FINGER_MCP].y and
                landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.RING_FINGER_MCP].y and
                landmark[Palm.PINKY_TIP].y > landmark[Palm.PINKY_MCP].y and
                landmark[Palm.THUMB_TIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x)

    def __isLetter_ЕL(self, landmark) -> bool:
        return (landmark[Palm.THUMB_TIP].x < landmark[Palm.THUMB_CMC].x and
                landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.INDEX_FINGER_MCP].x and
                landmark[Palm.MIDDLE_FINGER_TIP].x < landmark[Palm.MIDDLE_FINGER_MCP].x and
                landmark[Palm.RING_FINGER_TIP].x < landmark[Palm.RING_FINGER_MCP].x and
                landmark[Palm.PINKY_TIP].x < landmark[Palm.PINKY_MCP].x and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.INDEX_FINGER_MCP].y and
                landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.MIDDLE_FINGER_MCP].y and
                landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.RING_FINGER_MCP].y and
                landmark[Palm.PINKY_TIP].y > landmark[Palm.PINKY_MCP].y and
                landmark[Palm.THUMB_TIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x)
    def __isLetter_Ё(self, landmark) -> bool:
        pass

    def __isLetter_ЖR(self, landmark) -> bool:
        return (landmark[Palm.THUMB_TIP].x > landmark[Palm.THUMB_CMC].x and
                landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.INDEX_FINGER_MCP].x and
                landmark[Palm.MIDDLE_FINGER_TIP].x > landmark[Palm.MIDDLE_FINGER_MCP].x and
                landmark[Palm.RING_FINGER_TIP].x > landmark[Palm.RING_FINGER_MCP].x and
                landmark[Palm.PINKY_TIP].x > landmark[Palm.PINKY_MCP].x and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.INDEX_FINGER_MCP].y and
                landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.MIDDLE_FINGER_MCP].y and
                landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.RING_FINGER_MCP].y and
                landmark[Palm.PINKY_TIP].y > landmark[Palm.PINKY_MCP].y and
                landmark[Palm.THUMB_TIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x and
                landmark[Palm.THUMB_TIP].y > landmark[Palm.INDEX_FINGER_TIP].y)

    def __isLetter_ЖL(self, landmark) -> bool:
        return (landmark[Palm.THUMB_TIP].x < landmark[Palm.THUMB_CMC].x and
                landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.INDEX_FINGER_MCP].x and
                landmark[Palm.MIDDLE_FINGER_TIP].x < landmark[Palm.MIDDLE_FINGER_MCP].x and
                landmark[Palm.RING_FINGER_TIP].x < landmark[Palm.RING_FINGER_MCP].x and
                landmark[Palm.PINKY_TIP].x < landmark[Palm.PINKY_MCP].x and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.INDEX_FINGER_MCP].y and
                landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.MIDDLE_FINGER_MCP].y and
                landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.RING_FINGER_MCP].y and
                landmark[Palm.PINKY_TIP].y > landmark[Palm.PINKY_MCP].y and
                landmark[Palm.THUMB_TIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x and
                landmark[Palm.THUMB_TIP].y > landmark[Palm.INDEX_FINGER_TIP].y)
    def __isLetter_З(self, landmark) -> bool:
        pass
    def __isLetter_И(self, landmark) -> bool:
        return (landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.PINKY_TIP].y < landmark[Palm.THUMB_TIP].y) and \
               (0.8 < landmark[Palm.THUMB_TIP].y/landmark[Palm.INDEX_FINGER_TIP].y <1.2) and \
               (0.8 < landmark[Palm.THUMB_TIP].y/landmark[Palm.MIDDLE_FINGER_TIP].y <1.2)
    def __isLetter_Й(self, landmark) -> bool:
        pass
    def __isLetter_К(self, landmark) -> bool:
        pass
    def __isLetter_ЛR(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x / landmark[Palm.MIDDLE_FINGER_TIP].x < 0.8) and
                (landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y / landmark[Palm.RING_FINGER_TIP].y > 1.3) and
                (landmark[Palm.PINKY_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y))
    def __isLetter_ЛL(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x / landmark[Palm.MIDDLE_FINGER_TIP].x > 1.1) and
                (landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y / landmark[Palm.RING_FINGER_TIP].y > 1.3) and
                (landmark[Palm.PINKY_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y))
    def __isLetter_МR(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.RING_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x / landmark[Palm.RING_FINGER_TIP].x < 0.75) and
                (landmark[Palm.PINKY_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.RING_FINGER_TIP].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y / landmark[Palm.RING_FINGER_TIP].y < 1.3))
    def __isLetter_МL(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.RING_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x / landmark[Palm.RING_FINGER_TIP].x > 1.2) and
                (landmark[Palm.PINKY_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.RING_FINGER_TIP].y) and
                landmark[Palm.MIDDLE_FINGER_TIP].y / landmark[Palm.RING_FINGER_TIP].y < 1.3)
    def __isLetter_Н(self, landmark) -> bool:
        return (landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.PINKY_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y) and \
            (0.8 < landmark[Palm.THUMB_TIP].y / landmark[Palm.RING_FINGER_DIP].y < 1.2)
    def __isLetter_О(self, landmark) -> bool:
        pass
    def __isLetter_ПR(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x / landmark[Palm.MIDDLE_FINGER_TIP].x > 0.8) and
                (landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y / landmark[Palm.RING_FINGER_TIP].y > 1.3) and
                (landmark[Palm.PINKY_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y))

    def __isLetter_ПL(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x / landmark[Palm.MIDDLE_FINGER_TIP].x < 1.1) and
                (landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y / landmark[Palm.RING_FINGER_TIP].y > 1.3) and
                (landmark[Palm.PINKY_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y))
    def __isLetter_Р(self, landmark) -> bool:
        return (landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and
                landmark[Palm.PINKY_TIP].y < landmark[Palm.THUMB_TIP].y and
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y) and \
                (0.8 < landmark[Palm.THUMB_TIP].y / landmark[Palm.MIDDLE_FINGER_DIP].y < 1.2)
    def __isLetter_СR(self, landmark) -> bool:
        return (landmark[Palm.THUMB_TIP].x > landmark[Palm.THUMB_CMC].x and
                landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.INDEX_FINGER_MCP].x and
                landmark[Palm.MIDDLE_FINGER_TIP].x > landmark[Palm.MIDDLE_FINGER_MCP].x and
                landmark[Palm.RING_FINGER_TIP].x > landmark[Palm.RING_FINGER_MCP].x and
                landmark[Palm.PINKY_TIP].x > landmark[Palm.PINKY_MCP].x and
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.INDEX_FINGER_MCP].y and
                landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_MCP].y and
                landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.RING_FINGER_MCP].y and
                landmark[Palm.PINKY_TIP].y < landmark[Palm.PINKY_MCP].y)
    def __isLetter_СL(self, landmark) -> bool:
        return (landmark[Palm.THUMB_TIP].x < landmark[Palm.THUMB_CMC].x and
                landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.INDEX_FINGER_MCP].x and
                landmark[Palm.MIDDLE_FINGER_TIP].x < landmark[Palm.MIDDLE_FINGER_MCP].x and
                landmark[Palm.RING_FINGER_TIP].x < landmark[Palm.RING_FINGER_MCP].x and
                landmark[Palm.PINKY_TIP].x < landmark[Palm.PINKY_MCP].x and
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.INDEX_FINGER_MCP].y and
                landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.MIDDLE_FINGER_MCP].y and
                landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.RING_FINGER_MCP].y and
                landmark[Palm.PINKY_TIP].y < landmark[Palm.PINKY_MCP].y)
    def __isLetter_ТR(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.RING_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x / landmark[Palm.RING_FINGER_TIP].x > 0.75) and
                (landmark[Palm.PINKY_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.RING_FINGER_TIP].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y / landmark[Palm.RING_FINGER_TIP].y < 1.3))

    def __isLetter_ТL(self, landmark) -> bool:
        return ((landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.WRIST].y and
                 landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.WRIST].y) and
                (landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.RING_FINGER_TIP].x and
                 landmark[Palm.INDEX_FINGER_TIP].x / landmark[Palm.RING_FINGER_TIP].x < 1.3) and
                (landmark[Palm.PINKY_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.MIDDLE_FINGER_TIP].y and
                 landmark[Palm.PINKY_TIP].y < landmark[Palm.RING_FINGER_TIP].y and
                 landmark[Palm.MIDDLE_FINGER_TIP].y / landmark[Palm.RING_FINGER_TIP].y < 1.3))
    def __isLetter_У(self, landmark) -> bool:
        pass

    def __isLetter_ФR(self, landmark) -> bool:
        return (landmark[Palm.THUMB_TIP].x > landmark[Palm.THUMB_CMC].x and
                landmark[Palm.INDEX_FINGER_TIP].x > landmark[Palm.INDEX_FINGER_MCP].x and
                landmark[Palm.MIDDLE_FINGER_TIP].x > landmark[Palm.MIDDLE_FINGER_MCP].x and
                landmark[Palm.RING_FINGER_TIP].x > landmark[Palm.RING_FINGER_MCP].x and
                landmark[Palm.PINKY_TIP].x > landmark[Palm.PINKY_MCP].x and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.INDEX_FINGER_MCP].y and
                landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.MIDDLE_FINGER_MCP].y and
                landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.RING_FINGER_MCP].y and
                landmark[Palm.PINKY_TIP].y > landmark[Palm.PINKY_MCP].y and
                landmark[Palm.PINKY_TIP].x < landmark[Palm.MIDDLE_FINGER_TIP].x and
                landmark[Palm.THUMB_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y)

    def __isLetter_ФL(self, landmark) -> bool:
        return (landmark[Palm.THUMB_TIP].x < landmark[Palm.THUMB_CMC].x and
                landmark[Palm.INDEX_FINGER_TIP].x < landmark[Palm.INDEX_FINGER_MCP].x and
                landmark[Palm.MIDDLE_FINGER_TIP].x < landmark[Palm.MIDDLE_FINGER_MCP].x and
                landmark[Palm.RING_FINGER_TIP].x < landmark[Palm.RING_FINGER_MCP].x and
                landmark[Palm.PINKY_TIP].x < landmark[Palm.PINKY_MCP].x and
                landmark[Palm.INDEX_FINGER_TIP].y > landmark[Palm.INDEX_FINGER_MCP].y and
                landmark[Palm.MIDDLE_FINGER_TIP].y > landmark[Palm.MIDDLE_FINGER_MCP].y and
                landmark[Palm.RING_FINGER_TIP].y > landmark[Palm.RING_FINGER_MCP].y and
                landmark[Palm.PINKY_TIP].y > landmark[Palm.PINKY_MCP].y and
                landmark[Palm.PINKY_TIP].x > landmark[Palm.MIDDLE_FINGER_TIP].x and
                landmark[Palm.THUMB_TIP].y < landmark[Palm.INDEX_FINGER_TIP].y)
    def __isLetter_Х(self, landmark) -> bool:
        pass
    def __isLetter_Ц(self, landmark) -> bool:
        pass
    def __isLetter_Ч(self, landmark) -> bool:
        pass
    def __isLetter_Ш(self, landmark) -> bool:
        return (landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y) and \
            (0.8 < landmark[Palm.THUMB_TIP].y / landmark[Palm.PINKY_DIP].y < 1.2)
    def __isLetter_Щ(self, landmark) -> bool:
        pass
    def __isLetter_Ъ(self, landmark) -> bool:
        pass
    def __isLetter_Ы(self, landmark) -> bool:
        return (landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
         landmark[Palm.PINKY_TIP].y < landmark[Palm.THUMB_TIP].y) and \
        (0.8 < landmark[Palm.THUMB_TIP].y / landmark[Palm.RING_FINGER_DIP].y < 1.2) and \
        (0.8 < landmark[Palm.THUMB_TIP].y / landmark[Palm.MIDDLE_FINGER_DIP].y < 1.2)
    def __isLetter_Ь(self, landmark) -> bool:
        pass
    def __isLetter_Э(self, landmark) -> bool:
        pass
    def __isLetter_Ю(self, landmark) -> bool:
        pass
    def __isLetter_Я(self, landmark) -> bool:
        pass

if __name__ == '__main__':
    print('You should not run this file. Call main.py instead')