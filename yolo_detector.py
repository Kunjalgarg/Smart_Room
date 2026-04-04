from ultralytics import YOLO

class PersonTracker:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def track(self, frame):

        results = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            classes=[0]
        )

        persons = []

        if results[0].boxes.id is None:
            return persons

        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()
        classes = results[0].boxes.cls.cpu().numpy()

        for box, pid, cls in zip(boxes, ids, classes):

            # Detect only humans
            if int(cls) != 0:
                continue

            x1, y1, x2, y2 = map(int, box)

            persons.append({
                "id": int(pid),
                "bbox": (x1, y1, x2, y2)
            })

        return persons