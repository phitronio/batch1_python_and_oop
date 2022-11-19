import cv2
import mediapipe as mp
import serial
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()
arduino_commander = serial.Serial('COM3', 9600)
upper_lip_y = 0
lower_lip_y = 0
while True:
    _, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    face_landmarks = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if face_landmarks:
        landmarks = face_landmarks[0].landmark
        for id, landmark in enumerate(landmarks):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            if id == 0:
                upper_lip_y = y
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 14:
                lower_lip_y = y
                cv2.circle(frame, (x, y), 3, (0, 0, 255))
            if(lower_lip_y - upper_lip_y) > 20:
                print('mouth open')
                arduino_commander.write(b'o')
            else: 
                print('mouth close')
                arduino_commander.write(b'c')
    cv2.imshow('Automatic Eating', frame)
    cv2.waitKey(1)