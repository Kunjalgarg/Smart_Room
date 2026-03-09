import mediapipe as mp
import cv2
import numpy as np

class EyeDetector:

    def __init__(self):

        self.mesh = mp.solutions.face_mesh.FaceMesh(
            refine_landmarks=True)

        self.LEFT=[33,160,158,133,153,144]
        self.RIGHT=[362,385,387,263,373,380]

    def ear(self,landmarks,eye):

        p=[np.array(landmarks[i]) for i in eye]

        v1=np.linalg.norm(p[1]-p[5])
        v2=np.linalg.norm(p[2]-p[4])
        h=np.linalg.norm(p[0]-p[3])

        return (v1+v2)/(2*h)

    def detect(self,frame):

        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        res=self.mesh.process(rgb)

        if not res.multi_face_landmarks:
            return None

        h,w,_=frame.shape

        lm=[]

        for p in res.multi_face_landmarks[0].landmark:
            lm.append((int(p.x*w),int(p.y*h)))

        ear=(self.ear(lm,self.LEFT)+self.ear(lm,self.RIGHT))/2

        if ear<0.2:
            return "closed"

        return "open"