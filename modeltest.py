import tensorflow as tf
import numpy as np

TF_MODEL_FILE_PATH = 'model.tflite' # The default path to the saved TensorFlow Lite model

img_height = 384
img_width = 384
interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)

print(interpreter.get_signature_list())

classify_lite = interpreter.get_signature_runner('serving_default')
classify_lite

img = tf.keras.utils.load_img(
    'banana2.jpg', target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions_lite = classify_lite(input_1=img_array)['dense']
score_lite = tf.nn.softmax(predictions_lite)
class_names = ['banana', 'human']
print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score_lite)], 100 * np.max(score_lite))
)


