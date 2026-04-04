import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import serial
import cv2
import threading
import time

from yolo_detector import PersonTracker
# from pose_detector import PoseDetector
from eye_detector import EyeDetector
from sleep_logic import SleepLogic
from gui_light import LightGUI

print("Program started")

tracker = PersonTracker()
#pose = PoseDetector()
eyes = EyeDetector()
logic = SleepLogic()

last_person_seen = time.time()

gui = LightGUI()
#arduino = serial.Serial('COM7', 9600)
time.sleep(2)

print("Components initialized")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Camera failed to open")
    exit()

print("Camera initialized")


def vision_loop():

    print("Starting vision loop")

    global last_person_seen

    while gui.running:

        ret, frame = cap.read()

        if not ret or frame is None:
            continue

        persons = tracker.track(frame)

        # ----------- NO PERSON DETECTED -----------

        if len(persons) == 0:

            if time.time() - last_person_seen > 5:

                gui.light_off()

                cv2.putText(frame,
                            "ROOM EMPTY - LIGHT OFF",
                            (30, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            2)

            else:

                cv2.putText(frame,
                            "No person detected",
                            (30, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 255),
                            2)

        # ----------- PERSON DETECTED -----------

        else:

            last_person_seen = time.time()

            someone_awake = False

            for person in persons:

                pid = person["id"]
                bbox = person["bbox"]

                x1, y1, x2, y2 = bbox

                crop = frame[y1:y2, x1:x2]

                if crop is None or crop.size == 0:
                    continue

               # pose_state = pose.detect(crop)
                eye_state = eyes.detect(crop)

                sleep = logic.check_sleep(pid, eye_state, bbox)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                label = f"ID {pid} | {eye_state}"

                cv2.putText(frame,
                            label,
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (255, 255, 0),
                            2)

                if not sleep:
                    someone_awake = True

            # ----------- FINAL LIGHT DECISION -----------

            if someone_awake:

                gui.light_on()
                #arduino.write(b'1') #Turn bulb ON

                cv2.putText(frame,
                            "LIGHT ON",
                            (30, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2)

            else:

                gui.light_off()
                #arduino.write(b'0') #Turn bulb OFF

                cv2.putText(frame,
                            "LIGHT OFF - Sleeping",
                            (30, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            2)

        cv2.putText(frame,
                    f"Persons: {len(persons)}",
                    (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2)

        cv2.imshow("Smart Room AI", frame)

        if cv2.waitKey(1) == 27:
            gui.running = False
            break

    print("Exiting vision loop")

    cap.release()
    cv2.destroyAllWindows()


# =============================
# START SYSTEM
# =============================

vision_thread = threading.Thread(target=vision_loop)
vision_thread.daemon = True
vision_thread.start()

print("Vision thread started")

# Start GUI
gui.run()

print("Program closed")