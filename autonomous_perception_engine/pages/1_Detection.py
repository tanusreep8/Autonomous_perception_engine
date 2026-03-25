import streamlit as st
import cv2
import pandas as pd
import tempfile
from utils.detector import detect
from utils.tracker import Tracker

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(layout="wide")

# -------------------------------
# PREMIUM UI
# -------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🚗 Detection & Tracking")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.header("⚙️ Controls")
uploaded_file = st.sidebar.file_uploader("Upload Video", type=["mp4"])
confidence = st.sidebar.slider("Confidence", 0.1, 1.0, 0.5)

# -------------------------------
# LAYOUT
# -------------------------------
col1, col2 = st.columns([3, 1])

video_placeholder = col1.empty()

metric_total = col2.empty()
metric_unique = col2.empty()

# -------------------------------
# PROCESS VIDEO
# -------------------------------
if uploaded_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    cap = cv2.VideoCapture(tfile.name)

    tracker = Tracker()
    data = []
    unique_ids = set()

    frame_count = 0  # ⭐ IMPORTANT

    # Output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("output/output.mp4", fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))

        # -------------------------------
        # FRAME COUNT
        # -------------------------------
        frame_count += 1

        # -------------------------------
        # DETECTION
        # -------------------------------
        detections = detect(frame, confidence)

        boxes = [d[:4] for d in detections]
        tracked = tracker.update(boxes)

        for i, obj in enumerate(tracked):
            x1, y1, x2, y2, obj_id = obj
            label = detections[i][4]

            unique_ids.add(obj_id)

            # -------------------------------
            # STORE DATA (CSV)
            # -------------------------------
            data.append({
                "id": obj_id,
                "label": label,
                "frame": frame_count,
                "time": round(frame_count / 20, 2)  # assuming 20 FPS
            })

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{label}-{obj_id}",
                        (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0,255,0), 2)

        # Show video
        video_placeholder.image(frame, channels="BGR")

        # Save frame
        out.write(frame)

        # Metrics
        metric_total.metric("Total Detections", len(data))
        metric_unique.metric("Unique Objects", len(unique_ids))

    cap.release()
    out.release()

    # -------------------------------
    # SAVE CSV
    # -------------------------------
    df = pd.DataFrame(data)
    df.to_csv("output/data.csv", index=False)

    # -------------------------------
    # DOWNLOAD VIDEO
    # -------------------------------
    with open("output/output.mp4", "rb") as f:
        st.download_button("⬇️ Download Output Video", f)

    st.success("Processing Completed ✅")