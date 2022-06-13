# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PNXtmPnMMP8j7qSVXUi8_Zrm6s88rcQZ
"""

class Model:
  def __init__(self):
    import requests
    r = requests.get('https://github.com/magomartin/Prueba_IA_CNN_clasificar_imagen/blob/main/my_model.h5?raw=true')  
    with open('/content/mimodelo.h5', 'wb') as f:
      f.write(r.content)
    import tensorflow as tf
    global modelo
    modelo = tf.keras.models.load_model("/content/mimodelo.h5")
  def predict(self, file_path):
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    img = tf.keras.preprocessing.image.load_img(str(file_path), target_size=(250, 250))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  
    score = modelo(img_array)[0]
    return(np.argmax(score))