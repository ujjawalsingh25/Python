import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
draw_specification = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)

current_time = 0
prev_time = 0

# Loop
running = True
while running:                              # for running infinite till close the tab.

    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, face_landmarks, mpFaceMesh.FACEMESH_TESSELATION, draw_specification, draw_specification)

        for id, landmarks in enumerate(face_landmarks.landmark):
            # print(lm)
            img_height, img_width, ic = img.shape
            pos_x, pos_y = int(landmarks.x * img_width), int(landmarks.y * img_height)
            print(id, pos_x, pos_y)

    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(img, f'FPS : {(int(fps))}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)