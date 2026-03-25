from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect(frame, conf=0.5):
    results = model(frame, conf=conf)
    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if label in ["car", "person", "truck", "bus"]:
                detections.append([x1, y1, x2, y2, label])

    return detections