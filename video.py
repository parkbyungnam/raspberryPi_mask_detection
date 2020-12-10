from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from imutils.video import VideoStream
import matplotlib.pyplot as plt
import os
import time
import RPi.GPIO as GPIO
from time import sleep 

servoPin          = 12   # 서보 핀
SERVO_MAX_DUTY    = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY    = 3    # 서보의 최소(0도) 위치의 주기
myAngle = 0

GPIO.setmode(GPIO.BOARD)        # GPIO 설정
GPIO.setup(servoPin, GPIO.OUT)  # 서보핀 출력으로 설정

servo = GPIO.PWM(servoPin, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.

def setServoPos(degree):
  
  # 각도(degree)를 duty로 변경한다.
  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
  # duty 값 출력
  print("Gate is Open".format(degree, duty))

  # 변경된 duty값을 서보 pwm에 적용
  servo.ChangeDutyCycle(duty)



def Rotate(src, degrees):
    if degrees == 90:
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 1)

    elif degrees == 180:
        dst = cv2.flip(src, -1)

    elif degrees == 270:
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 0)
    else:
        dst = null
    return dst

facenet = cv2.dnn.readNet('models/deploy.prototxt', 'models/res10_300x300_ssd_iter_140000.caffemodel')
#2020.12.11.  일시수정
#model = load_model('models/mask_detector.model')
model = "converted_model.tflite"

#cap = cv2.VideoCapture('imgs/01.mp4')

IM_WIDTH = 480
IM_HEIGHT = 640
prev_time = 0
FPS = 24

cap = cv2.VideoCapture(-1)
cap.set(3,IM_WIDTH)
cap.set(4,IM_HEIGHT)


#ret, img = cap.read()

#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#out = cv2.VideoWriter('output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (img.shape[1], img.shape[0]))



while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    current_time = time.time() - prev_time
    if current_time >1./ FPS:
        prev_time = time.time()
        
        h, w = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, scalefactor=1., size=(300, 300), mean=(104., 177., 123.))
        facenet.setInput(blob)
        dets = facenet.forward()

        result_frame = frame.copy()

        for i in range(dets.shape[2]):
            confidence = dets[0, 0, i, 2]
            if confidence < 0.5:
                continue

            x1 = int(dets[0, 0, i, 3] * w)
            y1 = int(dets[0, 0, i, 4] * h)
            x2 = int(dets[0, 0, i, 5] * w)
            y2 = int(dets[0, 0, i, 6] * h)
            
            face = frame[y1:y2, x1:x2]

            face_input = cv2.resize(face, dsize=(224, 224))
            face_input = cv2.cvtColor(face_input, cv2.COLOR_BGR2RGB)
            face_input = preprocess_input(face_input)
            face_input = np.expand_dims(face_input, axis=0)
            
            mask, nomask = model.predict(face_input).squeeze()

            if mask > nomask:
                color = (0, 255, 0)
                label = 'Mask %d%%' % (mask * 100)
                
                if myAngle==0 and mask > 0.9:
                    myAngle=90
                    setServoPos(myAngle)#모터 90도 이동
                
                
            else:
                color = (0, 0, 255)
                label = 'No Mask %d%%' % (nomask * 100)
                
                if myAngle==90 and nomask < 0.5:
                    myAngle=0
                    setServoPos(myAngle)#모터 0도 이동

            cv2.rectangle(result_frame, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=color, lineType=cv2.LINE_AA)
            cv2.putText(result_frame, text=label, org=(x1, y1 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=color, thickness=2, lineType=cv2.LINE_AA)

        #out.write(result_img)
        result_frame = Rotate(result_frame, 270)
        cv2.imshow('result', result_frame)
        if cv2.waitKey(1) == ord('q'):
            break

out.release()
cap.release()
  # 서보 PWM 정지
servo.stop()
  # GPIO 모드 초기화
GPIO.cleanup()