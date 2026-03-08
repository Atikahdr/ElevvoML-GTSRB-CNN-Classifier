import numpy as np
import cv2
import tensorflow as tf

IMG_SIZE = 64

def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model


def preprocess_image(uploaded_file):

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = np.expand_dims(img, axis=0)

    return img


def predict_image(model, image):

    preds = model.predict(image, verbose=0)
    class_id = int(np.argmax(preds))
    confidence = float(np.max(preds))


    return class_id, confidence, preds[0]

