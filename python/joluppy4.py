import cv2
import sys 
import mediapipe as mp  
import math  
from serial import Serial
def distance(p1, p2):
    return math.dist((p1.x, p1.y), (p2.x, p2.y))  
arduino = Serial(
    port='COM8',
    baudrate=9600,
)


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands  

cap = cv2.VideoCapture(0) 

if not cap.isOpened():  
    print("Camera is not opened")
    sys.exit(1) 

hands = mp_hands.Hands()
d = ""
e = ""
while True: 
    res, frame = cap.read()

    if not res:  
        print("Camera error")
        break 

    frame = cv2.flip(frame, 1)  
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
    results = hands.process(image)  
    landmark_coords = []
    if results.multi_hand_landmarks:  
        for hand_landmarks in results.multi_hand_landmarks: 
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )

            points = hand_landmarks.landmark  

            fingers = 0  

            if distance(points[4], points[9]) > distance(points[3], points[9]):
                fingers += 1  

            for i in range(8, 21, 4):
                if distance(points[i], points[0]) > distance(points[i - 1], points[0]):
                    fingers += 1  

            if fingers == 0:  
                hand_shape = "s" 
            elif fingers == 1:  
                hand_shape = "motor 1" 
            elif fingers == 2:  
                hand_shape = "motor 2"  
            elif fingers == 3:  
                hand_shape = "motor 3"  
            else:  
                hand_shape = "" 
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
        c = "s"
        if d!= c:
            e = c.encode('utf-8')
            arduino.write(e)
            print(c)
        d = c
        #print("정지")
        continue
    cv2.imshow("MediaPipe Hands", frame)  #창모드 실행
    g = 0
    if(abs(landmark_coords[10][0]-landmark_coords[9][0])<5):
        g = abs((int(landmark_coords[10][1]-landmark_coords[9][1]))/2)
    key = cv2.waitKey(5) & 0xFF  
    if key == 27:  
        break 
    if(fingers):
      if(fingers == 1):
        c = "1"
      elif(fingers==2):
        c = "2"
      elif(fingers==3):
        c = "3"
      elif len(landmark_coords) >= 10:
        if fingers > 0:
            if abs(landmark_coords[5][0] - landmark_coords[9][0]) > abs(landmark_coords[5][1] - landmark_coords[9][1]):
                c = "f" if landmark_coords[5][0] > landmark_coords[9][0] else "b"
            else:
                c = "l" if landmark_coords[5][0] > landmark_coords[8][0] and landmark_coords[5][1] < landmark_coords[9][1] else "r"
        else:
            c = "s"
    else:
      c = "s"
    if d!= c:
        e = c.encode('utf-8')
        arduino.write(e)
        print(c)
    d = c

cv2.destroyAllWindows()
cap.release()