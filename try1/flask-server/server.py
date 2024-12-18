import sys
from flask import Flask, jsonify
import cv2
import mediapipe as mp
import math
import threading

app = Flask(__name__)
current_hand_shape = "settings...."
try1 = 0
lock1 = threading.Lock()
def distance(p1, p2):
    return math.dist((p1.x, p1.y), (p2.x, p2.y))

def initialize_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera is not opened")
        sys.exit(1)
    return cap

def process_frame(frame, hands, mp_drawing, mp_drawing_styles, mp_hands):
    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    return frame, image, results

def detect_hand_shape(points):
    fingers = 0
    if distance(points[4], points[9]) > distance(points[3], points[9]):
        fingers += 1
    for i in range(8, 21, 4):
        if distance(points[i], points[0]) > distance(points[i - 1], points[0]):
            fingers += 1
    return fingers

def get_hand_shape(fingers):
    if fingers == 0:
        return "stop"
    elif fingers == 1:
        return "motor 1"
    elif fingers == 2:
        return "motor 2"
    elif fingers == 3:
        return "motor 3"
    else:
        return ""

def draw_hand_landmarks(frame, hand_landmarks, mp_drawing, mp_drawing_styles, mp_hands):
    mp_drawing.draw_landmarks(
        frame,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_drawing_styles.get_default_hand_landmarks_style(),
        mp_drawing_styles.get_default_hand_connections_style(),
    )

def update_hand_shape():
    global current_hand_shape,try1
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    cap = initialize_camera()
    hands = mp_hands.Hands()

    d = ""
    while True:
        res, frame = cap.read()
        if not res:
            print("Camera error")
            break

        frame, image, results = process_frame(frame, hands, mp_drawing, mp_drawing_styles, mp_hands)
        landmark_coords = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                draw_hand_landmarks(frame, hand_landmarks, mp_drawing, mp_drawing_styles, mp_hands)
                points = hand_landmarks.landmark
                fingers = detect_hand_shape(points)
                hand_shape = get_hand_shape(fingers)
                current_hand_shape = hand_shape
                cv2.putText(
                    frame,
                    hand_shape,
                    (int(points[12].x * frame.shape[1]), int(points[12].y * frame.shape[0])),
                    cv2.FONT_HERSHEY_COMPLEX,
                    3,
                    (0, 255, 0),
                    5,
                )
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    landmark_coords.append((cx, cy))
        else:
            lock1.acquire()
            c = "stop"
            if d != c:
                current_hand_shape = c
                settry(1)
                print(gettry())
                print("update "+current_hand_shape)
            d = c
            lock1.release()
            continue

        cv2.imshow("MediaPipe Hands", frame)
        g = 0
        if len(landmark_coords) >= 10 and abs(landmark_coords[10][0] - landmark_coords[9][0]) < 5:
            g = abs((int(landmark_coords[10][1] - landmark_coords[9][1])) / 2)

        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break

        if fingers:
            if fingers == 1:
                c = "1"
            elif fingers == 2:
                c = "2"
            elif fingers == 3:
                c = "3"
            elif len(landmark_coords) >= 10:
                if fingers > 0:
                    if abs(landmark_coords[5][0] - landmark_coords[9][0]) > abs(landmark_coords[5][1] - landmark_coords[9][1]):
                        c = "front" if landmark_coords[5][0] > landmark_coords[9][0] else "back"
                    else:
                        c = "left" if landmark_coords[5][0] > landmark_coords[8][0] and landmark_coords[5][1] < landmark_coords[9][1] else "right"
                else:
                    c = "stop"
        else:
            c = "stop"
        lock1.acquire()
        if d != c:
            current_hand_shape = c
            settry(1)
            print(gettry())
            print("update "+current_hand_shape)
        lock1.release()
        d = c

    cv2.destroyAllWindows()
    cap.release()
def gettry():
    global try1
    return try1
def settry(a):
    global try1
    try1+=a

thred1 = threading.Thread(target=update_hand_shape)
@app.route('/users')
def users():
    global current_hand_shape
    print(gettry())
    print("user "+current_hand_shape)
    return jsonify({"val": current_hand_shape})

if __name__ == "__main__":
    thred1.start()
    app.run(debug=True)
