from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import time

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
model = load_model('models/mask_detector.model')

#cap = cv2.VideoCapture('imgs/01.mp4')
cap = cv2.VideoCapture(-1)
cap.set(3,480)
cap.set(4,640)
#ret, img = cap.read()

#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#out = cv2.VideoWriter('output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (img.shape[1], img.shape[0]))

prev_time = 0
FPS = 24

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
            else:
                color = (0, 0, 255)
                label = 'No Mask %d%%' % (nomask * 100)

            cv2.rectangle(result_frame, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=color, lineType=cv2.LINE_AA)
            cv2.putText(result_frame, text=label, org=(x1, y1 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=color, thickness=2, lineType=cv2.LINE_AA)

        #out.write(result_img)
        img= Rotate(result_frame,270)
        cv2.imshow('result', result_frame)
        if cv2.waitKey(1) == ord('q'):
            break

out.release()
cap.release()
