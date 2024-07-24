# Script que lee el archivo binario del modelo de red neuronal convolucional

#importación de librerias
import tensorflow as tf
from tensorflow.keras import models
tf.compat.v1.disable_eager_execution()
tf.compat.v1.experimental.output_all_intermediates(True)


#función para la importacion de la IA
def model_fun():
    model_cnn = tf.keras.models.load_model('conv_MLP_84.h5')
    return model_cnn