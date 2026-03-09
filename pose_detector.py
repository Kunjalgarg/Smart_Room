import mediapipe as mp
import cv2

class PoseDetector:

    def __init__(self):

        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(
        #     static_image_mode=False,
        #     model_complexity=1,
        #     enable_segmentation=False
        )

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.pose.process(rgb)

        if not results.pose_landmarks:
            return None

        lm = results.pose_landmarks.landmark

        nose = lm[0]
        shoulder = (lm[11].y + lm[12].y)/2

        diff = abs(nose.y - shoulder)

        if diff < 0.08:
            return "lying"

        return "upright"