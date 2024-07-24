#importación de librerias
import tensorflow as tf
import numpy as np

#Importación de modulos propios
from preprocess_img import preprocess
from load_model import model_fun
from integrador import predict

#pruebas

#probar que la predicción cumpla con la etiqueta, que sea un número flotante y el mapa de calor sea un arreglo numpy
def test_predict_salida():
    array = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
    label, proba, heatmap = predict(array)
    assert label in ["bacteriana", "normal", "viral"], "La etiqueta de predicción no es válida."
    assert isinstance(proba, float), "La probabilidad de predicción no es un flotante."
    assert isinstance(heatmap, np.ndarray), "El mapa de calor no es un arreglo numpy."

#Probar que la probabilidad de la predicción este entre 0% y 100%
def test_predict_probabilidad():
    array = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
    label, proba, heatmap = predict(array)
    print(proba)
    assert proba>=0.0 and proba<=100.0
    

#Probar que el normalizado del arreglo de datos este entre 0 y 1
def test_preprocess_normalizacion():
    array = np.random.randint(0, 255, (1024, 1024, 3), dtype=np.uint8)
    processed_array = preprocess(array)
    assert np.all(processed_array >= 0) and np.all(processed_array <= 1), "La normalización no es correcta, los datos no estan en [0,0]."

#Probar que el modelo cargue y que este sea una instancia keras
def test_model_fun_carga():
    model = model_fun()
    assert isinstance(model, tf.keras.Model), "El modelo no se cargó correctamente."
