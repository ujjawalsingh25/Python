import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

current_time = 0
prev_time = 0

# Loop
running = True
while running:                              # for running infinite till close the tab.

    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmarks.landmark):
                h, w, c = img.shape
                pos_x, pos_y = int(lm.x * w), int(lm.y *h)
                print(id, pos_x, pos_y)
                if id == 8:
                    cv2.circle(img, (pos_x, pos_y), 12, (0,0,0), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS)

    current_time = time.time()
    fps = 1/( current_time - prev_time)
    prev_time = current_time
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

