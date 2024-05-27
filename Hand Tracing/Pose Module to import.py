import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode =False, upBody = False, smooth = True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.hands
        self.Pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)
        self.pose = mp.solutions.pose

        # def findPose(self, img, draw=True):
        #     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #     self.results = self.hands.process(imgRGB)
        #
        #     if self.results.multi_hand_landmarks:
        #         for handLms in self.results.multi_hand_landmarks:
        #             if draw:
        #                 self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        #     return img

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            pos_x, pos_y = int(lm.x * w), int(lm.y * h)
            print(id, pos_x, pos_y)
            if id == 11 or id == 12:
                cv2.circle(img, (pos_x, pos_y), 10, (0, 0, 0), cv2.FILLED)

        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)


def main():
    cap = cv2.VideoCapture('video1.mp4')

    current_time = 0
    prev_time = 0

    running = True
    while running:  # for running infinite till close the tab.
        success, img = cap.read()

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(10)


if __name__ == "__main__":
    main()