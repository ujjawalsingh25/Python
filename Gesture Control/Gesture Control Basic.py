import cv2
import time
import math
import numpy as np
import Hand_Tracking as hand_track
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# import ctypes import cast, POINTER

wCam , hCam = 640, 480

cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

current_time = 0
prev_time = 0

detector = hand_track.HandDetector(detectionCon = 0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()

volume_range = (volume.GetVolumeRange())                  # Give a volume range of (--60 to 0.0)
# volume.SetMasterVolumeLevel(0.0, None)        # Sets the volume in the given parameter range if it is 0 then 100 or 10 then vol is 50.
minVol = volume_range[0]
maxVol = volume_range[1]
vol =0
volBar =400
volPercentage = 0

# Loop
running = True
while running:                              # for running infinite till close the tab.

    success, img = cap.read()
    img = detector.findHands(img)                      # Use to find hands and getting the image back.
    lmList = detector.findPosition(img, draw= False)    # Since we already drawing so false
    if len(lmList) != 0:                    # when no hand detects so landmark list do not have any index.
        # print(lmList[4] , lmList[8])

        x1, y1 = lmList[4][1] , lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx , cy = (x1+x2)//2 , (y1+y2)//2
        cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)
        cv2.circle(img, (cx, cy), 8, (0, 0, 0), cv2.FILLED)       # 8 is the radius

        length = math.hypot(x2 - x1 , y2 - y1)              # To get the distance between points.
        # print(length)

        # Hand range = 20 to 220
        # Volume Range = -65 to 0

        vol = np.interp(length, [20,180], [minVol, maxVol])
        volBar = np.interp(length, [20, 180], [400, 150])
        volPercentage = np.interp(length, [20, 180], [0, 100])
        print(int(length), int(vol))

        volume.SetMasterVolumeLevel(vol,None)  # Sets the volume in the given parameter range
                                                    # if it is 0 then 100 or 10 then vol is 50.

        if length <25:
            cv2.circle(img, (cx, cy), 8, (255, 0, 255), cv2.FILLED)

        cv2.rectangle(img, (50, 150), (85, 400), (0,0,0), 4)
        cv2.rectangle(img, (50,int(volBar)), (85,400), (0,0,0), cv2.FILLED)
        cv2.putText(img, f'Vol : {(int(volPercentage))} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)


    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(img, f'FPS : {(int(fps))}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0 , 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)