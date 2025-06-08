import cv2
import mediapipe as mp
import pygame
import os

# Setup for mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam setup
cap = cv2.VideoCapture(0)

# Song folder path
SONG_FOLDER = "songs"
songs = [f for f in os.listdir(SONG_FOLDER) if f.endswith(".mp3")]

# Pygame music setup
pygame.mixer.init()
song_playing = False
current_song_index = 0

# Finger tips for detection
finger_tips = [4, 8, 12, 16, 20]

# Colors
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
HEADER_COLOR = (0, 255, 180)
HIGHLIGHT_COLOR = (255, 255, 0)

# Instructions
instructions = [
    "✌️  2 Fingers  - Show Song List",
    "🤟  3 Fingers  - Play Current Song",
    "🖖  4 Fingers  - Next Song",
    "🖐️  5 Fingers  - Stop Song",
    "🔴  Press 'Q' to Quit"
]

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Mirror view
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    fingers = []

    # Draw background for instructions
    cv2.rectangle(img, (0, 0), (640, 160), BG_COLOR, -1)

    # Header
    cv2.putText(img, "🎵 Finger Gesture Music Controller 🎵", (10, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, HEADER_COLOR, 2)

    # Show instructions
    for i, line in enumerate(instructions):
        cv2.putText(img, line, (10, 60 + i * 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, TEXT_COLOR, 1)

    # Show currently playing song (always on screen)
    if song_playing:
        cv2.putText(img, f"🎧 Now Playing: {songs[current_song_index]}", (10, 460),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 100), 2)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = []

            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            # Thumb
            if lm_list[finger_tips[0]][0] > lm_list[finger_tips[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers
            for tip in finger_tips[1:]:
                if lm_list[tip][1] < lm_list[tip - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = fingers.count(1)

            # Show finger count
            cv2.rectangle(img, (10, 320), (250, 360), (0, 0, 0), -1)
            cv2.putText(img, f'Fingers Detected: {total_fingers}', (20, 350),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, HIGHLIGHT_COLOR, 2)

            # Gesture actions
            if total_fingers == 2:
                y_pos = 180
                cv2.putText(img, "🎵 Song List:", (20, y_pos),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                for i, song in enumerate(songs):
                    y_pos += 25
                    cv2.putText(img, f"{i+1}. {song}", (20, y_pos),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 0), 1)

            elif total_fingers == 3:
                if not song_playing and songs:
                    song_path = os.path.join(SONG_FOLDER, songs[current_song_index])
                    try:
                        pygame.mixer.music.load(song_path)
                        pygame.mixer.music.play()
                        song_playing = True
                    except:
                        pass
                cv2.putText(img, f"🎧 Playing: {songs[current_song_index]}", (20, 430),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

            elif total_fingers == 4:
                if songs:
                    current_song_index = (current_song_index + 1) % len(songs)
                    song_path = os.path.join(SONG_FOLDER, songs[current_song_index])
                    try:
                        pygame.mixer.music.load(song_path)
                        pygame.mixer.music.play()
                        song_playing = True
                    except:
                        pass
                cv2.putText(img, f"⏭️  Next: {songs[current_song_index]}", (20, 430),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 128, 255), 2)

            elif total_fingers == 5:
                if song_playing:
                    pygame.mixer.music.stop()
                    song_playing = False
                cv2.putText(img, "⛔ Music Stopped", (20, 430),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 100, 255), 2)

            # Draw hand
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Finger Music Player", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
