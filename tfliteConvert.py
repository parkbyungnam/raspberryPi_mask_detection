import tensorflow as tf

coverter = tf.lite.TFLiteConverter.from_saved_model(r'models')
tflite_model = converter.convert()

with open('modelTest.tflite','wb') as f:
    f.write(tflite_model)