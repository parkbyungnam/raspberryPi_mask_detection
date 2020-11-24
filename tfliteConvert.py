from tensorflow import keras

model = keras.models.load_model('models/mask_detector.model',compile=False)
export_path = 'models/'
model.save(export_path,save_format = 'tf')

import tensorflow as tf

saved_model_dir = 'models/'
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops=[tf.lite.OpsSet.TFLITE_BUILTINS,tf.lite.OpsSet.SELECT_TF_OPS]
tflite_model = converter.convert()
open('models/converted_model.tflite','wb').write(tflite_model)