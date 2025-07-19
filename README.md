# 🧍 Real-Time Fall Detection with YOLOv8 + Streamlit + WebRTC

This project is a real-time fall detection system built using [Ultralytics YOLOv8 pose estimation](https://docs.ultralytics.com/tasks/pose/) and [Streamlit](https://streamlit.io/) for the frontend interface. It captures live webcam video, detects human poses using keypoints, and triggers an alert (sound and visual) if a potential fall is detected based on body orientation.

---

## 🚀 Live Demo

🎯 Try the real-time app here:  
👉 **[Open Live App](https://yolo-fall-detection-6q6mqkckydxp44akmtcsmh.streamlit.app/)**

> Works on both **desktop** and **mobile browsers** (with camera permission enabled).

---

## 📸 Use Case

Falls are a major health concern for elderly people, patients in hospitals, and workers in high-risk environments. This system can be integrated into:

- 🧓 Elderly care facilities
- 🏥 Hospitals and clinics
- 🧱 Industrial safety monitoring
- 🏠 Smart homes

---

## 🧠 How It Works

The app uses YOLOv8 Pose to detect 17 keypoints on the human body. It then checks the **relative orientation** between the **shoulder and hip** keypoints:

- If the **horizontal distance** is greater than the **vertical distance** (i.e., person lying flat), it assumes a **fall** has occurred.
- When a fall is detected:
  - A warning message is shown: `"⚠️ FALL DETECTED!"`
  - An alert sound (`alert.mp3`) plays automatically.

---

## 🛠 Features

- 📷 **Live Webcam Feed**: Uses `streamlit-webrtc` for real-time streaming in browser.
- 👁️ **Pose Estimation**: Based on Ultralytics `yolov8n-pose.pt` model.
- 🧠 **Fall Detection Logic**: Simple but effective check using shoulder and hip positions.
- 🔔 **Sound Alert**: MP3 sound plays on browser when fall is detected.
- ✅ Works on **laptop and mobile browsers**.

