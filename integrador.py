#Es un módulo que integra los demás scripts y retorna solamente lo necesario para ser visualizado en la interfaz gráfica.
#Retorna la clase, la probabilidad y una imagen el mapa de calor generado por Grad-CAM.

#importacion de librerias
import numpy as np
import load_model
import preprocess_img
import grad_cam




def predict(array):
    #   1. call function to pre-process image: it returns image in batch format
    batch_array_img = preprocess_img.preprocess(array)
    
    #   2. call function to load model and predict: it returns predicted class and probability
    model = load_model.model_fun()
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    label = ""
    if prediction == 0:
        label = "bacteriana"
    if prediction == 1:
        label = "normal"
    if prediction == 2:
        label = "viral"
    #   3. call function to generate Grad-CAM: it returns an image with a superimposed heatmap
    heatmap = grad_cam.grad_cam(array)
    return (label, proba, heatmap)
