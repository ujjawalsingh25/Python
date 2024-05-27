import cv2
import mediapipe as mp
import time

class face_mesh_detector():
    def __init__(self, static_image_mode=False, max_faces=1, detection_confidence=0.5, tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_faces = max_faces
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode=self.static_image_mode,
            max_num_faces=self.max_faces,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence)
        self.draw_specification = self.mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)
        # Highlight points with given thickness, circle_radius and color.

    def find_face_mesh(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        multiple_faces = []
        if self.results.multi_face_landmarks:
            for face_landmarks in self.results.multi_face_landmarks:
                # For Drawing the points
                if draw:
                    # Draw the face landmarks with connection
                    # self.mpDraw.draw_landmarks(img, face_landmarks, self.mpFaceMesh.FACEMESH_TESSELATION,
                    #                            self.draw_specification, self.draw_specification)

                    # Draw only the face landmarks without connection
                    self.mpDraw.draw_landmarks(img, face_landmarks, self.mpFaceMesh.FACEMESH_FACE_OVAL,
                                               self.draw_specification, self.draw_specification)

                #  For getting points and if required draw (commented) id points on face.
                single_face = []
                for id, landmarks in enumerate(face_landmarks.landmark):
                    img_height, img_width, ic = img.shape
                    pos_x, pos_y = int(landmarks.x * img_width), int(landmarks.y * img_height)
                    print(id, pos_x, pos_y)
                    # cv2.putText(img, str(id ), (pos_x, pos_y), cv2.FONT_HERSHEY_PLAIN, 0.4, (0, 255, 0), 1)
                            # To print the id no's on the face.
                    single_face.append((pos_x, pos_y))
                multiple_faces.append(single_face)

        return img, multiple_faces

def main():
    cap = cv2.VideoCapture('video2.mp4')
    detector = face_mesh_detector(max_faces = 2)     # By default it takes 1 or check for 1 faces but here changed for 2 faces.

    current_time = 0
    prev_time = 0

    # Loop
    running = True
    while running:
        success, img = cap.read()
        if not success:
            break

        img, multiple_faces = detector.find_face_mesh(img, True)

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        cv2.putText(img, f'FPS : {(int(fps))}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
