import cv2
import mediapipe as mp
import time

class face_mesh_detector():
    def __int__(self, static_image_mode = False, max_faces = 1, detection_confidence = 0.5, tracking_confidence = 0.5):
        self.static_image_mode = static_image_mode
        self.max_faces = max_faces
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.static_image_mode, self.max_faces, self.detection_confidence, self.tracking_confidence)
        self.draw_specification = self.mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)

    def find_face_mesh(self, img, draw = True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        multiple_faces = []
        if self.results.multi_face_landmarks:
            for face_landmarks in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, face_landmarks, self.mpFaceMesh.FACEMESH_TESSELATION,
                                               self.draw_specification, self.draw_specification)
            single_face = []
            for id, landmarks in enumerate(face_landmarks.landmark):
                # print(landmarks)
                img_height, img_width, ic = img.shape
                pos_x, pos_y = int(landmarks.x * img_width), int(landmarks.y * img_height)
                print(id, pos_x, pos_y)
                single_face.append(pos_x, pos_y)
            multiple_faces.append(single_face)

            return img, multiple_faces

def main():
    cap = cv2.VideoCapture('video2.mp4')
    detector = face_mesh_detector()

    current_time = 0
    prev_time = 0

    # Loop
    running = True
    while running:  # for running infinite till close the tab.

        success, img = cap.read()
        img, multiple_faces = detector.find_face_mesh(img, False)

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        cv2.putText(img, f'FPS : {(int(fps))}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()

