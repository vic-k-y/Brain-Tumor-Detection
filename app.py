import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras import models,layers

cnnmodel = keras.models.load_model("cnnmodel2")

def to_predict(img):
  img_array = tf.keras.preprocessing.image.img_to_array(img)
  img_array = tf.expand_dims(img_array, 0)
  predictions = cnnmodel.predict(img_array)
  conf= {}
  for i in range(4):
    #print ("%.16f" % (float(i)))
    conf[classes[i]]= float("%.4f" % (float(predictions[0][i])))
  return conf

import gradio as gr


iface=gr.Interface(fn=to_predict,
             inputs=gr.Image(),
             outputs=gr.Label(num_top_classes=3),
             examples=["images/image(9).jpg","images/image.jpg","images/p (1).jpg","images/gg (1).jpg"])

iface.launch()
    
