import tensorflow.lite as lite

input_file = "mask_detector.model"
output_file = "mask_detector.tflite"

converter = lite.TocoConverter.from_keras_model_file(input_file)
tflite_model = converter.convert()
open(output_file, "wb").write(tflite_model)