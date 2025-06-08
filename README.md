
# 🎵 Finger Gesture Music Controller

A Python-based project that uses **hand gestures** to control music playback using your webcam. This system enables **touchless interaction** with your music player using **MediaPipe for gesture detection** and **Pygame for audio playback**.

---

## 🧠 Features

- ✌️ **2 Fingers** – Show available songs  
- 🤟 **3 Fingers** – Play the current song  
- 🖖 **4 Fingers** – Play the next song  
- 🖐️ **5 Fingers** – Stop the music  
- 🎧 Displays the name of the current song playing  
- 🔴 Press **Q** to quit the application  

---

## 🛠 Technologies Used

- **OpenCV** – for capturing webcam frames  
- **MediaPipe** – for detecting and tracking hand landmarks  
- **Pygame** – for playing audio files  
- **Python** – main programming language  

---

## 📂 Folder Structure

```
FingerGestureMusicController/
├── songs/                # Folder containing .mp3 songs
├── main.py               # Main Python script
├── README.md             # Project overview
```

---

## 📦 Requirements

Install dependencies with:

```bash
pip install opencv-python mediapipe pygame
```

---

## ▶️ How to Run

1. Place all your `.mp3` files in a folder named **`songs`** inside your project directory.
2. Run the script:

```bash
python main.py
```

3. Show hand gestures in front of your webcam to control the player.

---

## 💡 Use Cases

- Hands-free music control while **cooking, cleaning, or exercising**
- Assistive tech for **physically challenged users**
- Smart mirror or interactive kiosk systems

---

## 📌 Notes

- Ensure good lighting and hand visibility for better gesture recognition.
- The webcam must be working properly.

---

## 📜 License

This project is for educational/demo purposes. Customize it as needed for your use case.
