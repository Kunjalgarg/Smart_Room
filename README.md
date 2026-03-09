# 🧠 Smart Room AI

### Vision-Based Sleep Detection & Intelligent Light Automation

![Python](https://img.shields.io/badge/Python-3.11.9-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-red)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose%20Tracking-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An **AI-powered smart room automation system** that uses **Computer Vision to understand human behavior** and automatically control lighting based on **sleep state, presence, and activity**.

Unlike traditional smart systems that rely on **motion sensors**, this project uses **deep learning and pose analysis** to determine whether people are **awake, sleeping, or absent**.

---

# 🚀 Features

✔ **Real-time person detection** using YOLO
✔ **Multi-person tracking** with unique IDs
✔ **Pose detection** to detect sleeping posture
✔ **Eye state detection** (open / closed)
✔ **Behavior-based sleep detection logic**
✔ **Automatic smart light control**
✔ **Room empty detection**
✔ **Live visual monitoring interface**

---

# 🧠 How the System Thinks

The system doesn't just detect motion — it **understands human behavior**.

## Decision Logic

| Situation                          | System Action |
| ---------------------------------- | ------------- |
| Person detected and awake          | 💡 Light ON   |
| Person lying down with closed eyes | 🔴 Light OFF  |
| All persons sleeping               | 🔴 Light OFF  |
| Room empty for 5 seconds           | 🔴 Light OFF  |
| Person inactive for 10 minutes     | 🔴 Light OFF  |
| Multiple people (one awake)        | 💡 Light ON   |

---

# 🏗 System Architecture

```
Webcam Input
      │
      ▼
YOLO Person Detection
      │
      ▼
Person Tracking (Unique IDs)
      │
      ▼
Pose Detection
      │
      ▼
Eye Detection
      │
      ▼
Sleep Detection Logic
      │
      ▼
Smart Light Controller
```

---

# 📸 Example Output

### Real-time Detection Interface

![Image](https://cynapps-thedatafrog.s3.amazonaws.com/media/images/Screen-Shot-2019-04-18-at-16.15.54.original.png)

The interface shows:

* Person bounding boxes
* Pose state
* Eye state
* Light status
* Real-time camera feed

---

# 📂 Project Structure

```
smart-room-ai/

main.py               # Main execution script
yolo_detector.py      # Person detection & tracking
pose_detector.py      # Body pose detection
eye_detector.py       # Eye state detection
sleep_logic.py        # AI sleep decision logic
gui_light.py          # Light control GUI

requirements.txt
README.md
LICENSE
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Kunjalgarg/Smart_Room
cd smart_light_cv
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

Your webcam will start and the **Smart Room AI system will begin monitoring the room**.

---

# 🧰 Tech Stack

### Programming

* Python

### Computer Vision

* OpenCV
* YOLOv8 (Ultralytics)
* MediaPipe

### AI Techniques Used

* Object Detection
* Multi-object tracking
* Pose estimation
* Facial landmark detection
* Behavioral logic systems

### Interface

* Tkinter GUI
* OpenCV visualization

---

# 🔮 Future Improvements

Planned upgrades to extend the system into a **full smart home AI system**.

* 📡 ESP32 smart bulb control
* 👤 Face recognition for user profiles
* 🌙 Night vision / low-light detection
* 🧠 Deep learning sleep detection
* 📊 Smart home dashboard
* 🏠 Home Assistant integration

---

# 🎯 Applications

This system can be used for:

🏠 Smart homes
🧓 Elderly monitoring systems
⚡ Energy saving automation
🏫 Smart dormitories
🛏 AI sleep monitoring systems

---

# ⭐ Why This Project is Interesting

Most smart lighting systems rely on **motion sensors**.

This project instead uses **Artificial Intelligence to interpret human behavior**.

This allows the system to understand situations like:

* Someone **sleeping**
* Someone **resting but awake**
* The **room being empty**

The result is a **context-aware intelligent room**.

---

# 👨‍💻 Author

Kunjal Garg
Developed as a **Computer Vision and Intelligent Automation project** exploring how AI can make everyday environments smarter.

---

⭐ If you find this project interesting, consider **starring the repository**.
