import time
import numpy as np

class SleepLogic:

    def __init__(self):

        self.eye_closed_time={}
        #self.last_positions={}
        self.position_time={}

    def check_sleep(self, person_id, eye, bbox):

        x1,y1,x2,y2 = bbox

        center = ((x1+x2)//2, (y1+y2)//2)

        now = time.time()

        # Initialize dictionaries for new person
        if person_id not in self.eye_closed_time:
            self.eye_closed_time[person_id] = None
            #self.last_positions[person_id] = center
            self.position_time[person_id] = now

        # Movement detection
        # dist = np.linalg.norm(
        #      np.array(center) - np.array(self.last_positions[person_id])
        #)

        # if dist > 20:
        #     self.position_time[person_id] = now

        # self.last_positions[person_id] = center

        # 10 minute inactivity rule
        # if now - self.position_time[person_id] > 600:
        #     return True

        # Eye + pose sleep rule
        if eye == "closed":

            if self.eye_closed_time[person_id] is None:
                self.eye_closed_time[person_id] = now

            if now - self.eye_closed_time[person_id] > 5:
                return True

        else:
            self.eye_closed_time[person_id] = None

        return False