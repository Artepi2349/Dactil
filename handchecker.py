from palm import Palm
#from main import hand

class HandChecker:

    sel_hand = ''
    rotate = ''
    fingers = ''

    def __init__(self, h):
        self.sel_hand = h

    def checkHand(self, landmark):
        if self.__fingersUp(self, landmark):
            fingers = 'Up'
        if self.__fingersDown(self, landmark):
            fingers = 'Down'
        if self.__fingersMiddle(self, landmark):
            fingers = 'Middle'

        if self.__rotateBackR(self, landmark) or self.__rotateBackL(self, landmark):
            rotate = 'Back'
        if self.__rotateFrontR(self, landmark) or self.__rotateFrontL(self, landmark):
            rotate = 'Front'
        if self.__rotateMiddleR(self, landmark) or self.__rotateMiddleL(self, landmark):
            rotate = 'Middle'
    # Private functions
    def __fingersUp(self,landmark) -> bool:
        return landmark[Palm.MIDDLE_FINGER_MCP].y / landmark[Palm.WRIST].y > 1.2
    def __fingersDown(self, landmark) -> bool:
        return landmark[Palm.MIDDLE_FINGER_MCP].y / landmark[Palm.WRIST].y < 0.85
    def __fingersMiddle(self, landmark) -> bool:
        return 0.85 < landmark[Palm.MIDDLE_FINGER_MCP].y / landmark[Palm.WRIST].y < 1.2

    def __rotateFrontR(self,landmark) -> bool:
        return self.sel_hand=='R' and landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 0.8
    def __rotateBackR(self,landmark) -> bool:
        return self.sel_hand=='R' and landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x > 1.25
    def __rotateMiddleR(self,landmark) -> bool:
        return self.sel_hand=='R' and 0.8 < landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 1.25


    def __rotateFrontL(self,landmark) -> bool:
        return self.sel_hand=='L' and landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x > 1.25
    def __rotateBackL(self,landmark) -> bool:
        return self.sel_hand=='L' and landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 0.8
    def __rotateMiddleL(self,landmark) -> bool:
        return self.sel_hand=='L' and 0.8 < landmark[Palm.INDEX_FINGER_MCP].x / landmark[Palm.PINKY_MCP].x < 1.25

if __name__ == '__main__':
    print('You should not run this file. Call main.py instead')