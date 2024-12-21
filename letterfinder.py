#!/usr/bin/python3

from palm import Palm

class LetterFinder:
    """
    Здесь собраны фунции для определения буквы, которую показывает пользователь
    """

    def __init__(self):
        pass

    def getLetter(self, hand, rotate, fingers, landnmark) -> str:
        """
        Функуия для выбора буквы
        :param hand: Рука, выбранная пользователем
        :param rotate: Положение ладони в пространстве
        :param fingers: Поворот пальцев
        :param landnmark: Массив координат точек на ладони
        """

        if self.__isLetter_Ы(landnmark):
            return 'Ы'
        if self.__isLetter_И(landnmark):
            return 'И'
        if self.__isLetter_Н(landnmark):
            return 'Н'
        if self.__isLetter_Ш(landnmark):
            return 'Ш'
        if self.__isLetter_Р( landnmark):
            return 'Р'
        if hand == 'R':
            if self.__isLetter_ВR( landnmark):
                return 'В'
        if hand == 'L':
            if self.__isLetter_ВL(landnmark):
                return 'В'
        return ''

    # Private functions
    def __isLetter_А(self, landmark) -> bool:
        pass
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
    def __isLetter_Г(self, landmark) -> bool:
        pass
    def __isLetter_Д(self, landmark) -> bool:
        pass
    def __isLetter_Е(self, landmark) -> bool:
        pass
    def __isLetter_Ё(self, landmark) -> bool:
        pass
    def __isLetter_Ж(self, landmark) -> bool:
        pass
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
    def __isLetter_Л(self, landmark) -> bool:
        pass
    def __isLetter_М(self, landmark) -> bool:
        pass
    def __isLetter_Н(self, landmark) -> bool:
        return (landmark[Palm.MIDDLE_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.PINKY_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y) and \
            (0.8 < landmark[Palm.THUMB_TIP].y / landmark[Palm.RING_FINGER_DIP].y < 1.2)
    def __isLetter_О(self, landmark) -> bool:
        pass
    def __isLetter_П(self, landmark) -> bool:
        pass
    def __isLetter_Р(self, landmark) -> bool:
        return (landmark[Palm.RING_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.PINKY_TIP].y < landmark[Palm.THUMB_TIP].y and \
                landmark[Palm.INDEX_FINGER_TIP].y < landmark[Palm.THUMB_TIP].y) and \
            (0.8 < landmark[Palm.THUMB_TIP].y / landmark[Palm.MIDDLE_FINGER_DIP].y < 1.2)
    def __isLetter_С(self, landmark) -> bool:
        pass
    def __isLetter_Т(self, landmark) -> bool:
        pass
    def __isLetter_У(self, landmark) -> bool:
        pass
    def __isLetter_Ф(self, landmark) -> bool:
        pass
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
