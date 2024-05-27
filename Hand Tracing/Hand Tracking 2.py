import cv2
import mediapipe as mp
import time

class hand_detector():
    def __init__(self, mode = False, max_hands = 2, detection_confidence = 0.5, tracking_confidence = 0.5):
        self.mode = mode                                       # the obj that will be created will be assigned
        self.max_hands = max_hands                              # with the parameter value. Self will be like
        self.detection_confidence = detection_confidence           # obj.mode = mode_value i.e False
        self.tracking_confidence = tracking_confidence

        self.mpHands = mp.solutions.hands                           # initialise these values for the for the obj as required
        # self.hands = self.mpHands.Hands(self.mode, self.max_hand, self.detection_confidence, self.tracking_confidence)
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.detection_confidence, self.tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils                        # to get the hand detection.

    def find_hands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLandmarks in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLandmarks, self.mpHands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_no = 0, draw = True):
        landmark_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                pos_x, pos_y = int(lm.x * w), int(lm.y * h)
                # print(id, pos_x, pos_y)
                landmark_list.append([id, pos_x, pos_y])
                if draw:
                    cv2.circle(img, (pos_x, pos_y), 12, (0, 0, 0), cv2.FILLED)
        return landmark_list
# def main():
#     current_time = 0
#     prev_time = 0
#
#     cap = cv2.VideoCapture(0)
#     detector = hand_detector()
#     # detector = hand_detector()          # obj 'detector' passed to constructor 'hand_detector' with default parameter
#     running = True
#     while running:  # for running infinite till close the tab.
#
#         success, img = cap.read()
#         img = detector.find_hands(img)
#         landmark_list = detector.find_position(img)
#         if len(landmark_list) != 0:
#             print(landmark_list[8])
#
#         current_time = time.time()
#         fps = 1 / (current_time - prev_time)
#         prev_time = current_time
#         cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
#
#         cv2.imshow("Image", img)
#         cv2.waitKey(1)
#
#
# if __name__ == "__main__":
#     main()
#
