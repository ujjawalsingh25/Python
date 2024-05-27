import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture('video1.mp4')

current_time = 0
prev_time = 0

running = True
while running:                              # for running infinite till close the tab.
    success, img = cap.read()
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

    # if results.multi_hand_landmarks:
        # for handLandmarks in results.multi_hand_landmarks:
        #     for id, lm in enumerate(handLandmarks.landmark):
        #         h, w, c = img.shape
        #         pos_x, pos_y = int(lm.x * w), int(lm.y * h)
        #         print(id, pos_x, pos_y)
        #         if id == 8:
        #             cv2.circle(img, (pos_x, pos_y), 12, (0, 0, 0), cv2.FILLED)
        #     mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS)

    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(10)

