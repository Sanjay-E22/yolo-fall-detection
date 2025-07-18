import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, ClientSettings
from ultralytics import YOLO
import av
import cv2
import numpy as np
import threading

st.set_page_config(page_title="Fall Detection", layout="centered")
st.title("🧍 Real-Time Fall Detection using YOLOv8 + Webcam")
st.markdown("Live webcam pose estimation with fall alert + sound (mobile/laptop supported).")

model = YOLO("weights/yolov8n-pose.pt")

# Inject alert sound (HTML audio)
alert_placeholder = st.empty()
alert_audio = """
<audio autoplay>
  <source src="alert.mp3" type="audio/mpeg">
</audio>
"""

# Thread-safe sound trigger
fall_trigger = {"alert": False}
lock = threading.Lock()

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        image = frame.to_ndarray(format="bgr24")
        results = model(image)
        annotated = results[0].plot()

        fall = False
        for keypoints in results[0].keypoints.data:
            kp = keypoints.cpu().numpy()
            if len(kp) > 11:
                shoulder = kp[5]
                hip = kp[11]
                if abs(hip[1] - shoulder[1]) < abs(hip[0] - shoulder[0]):
                    cv2.putText(annotated, "⚠️ FALL DETECTED!", (20, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
                    fall = True

        with lock:
            fall_trigger["alert"] = fall

        return av.VideoFrame.from_ndarray(annotated, format="bgr24")

# Start webcam
webrtc_streamer(
    key="fall-detection",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)

# Play sound if fall detected
while True:
    with lock:
        if fall_trigger["alert"]:
            alert_placeholder.markdown(alert_audio, unsafe_allow_html=True)
            fall_trigger["alert"] = False
