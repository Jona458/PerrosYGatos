import numpy as np
import keras
import tensorflow
import pillow



args = {
    
    "model": "RedCNN_PerrosyGatos.h5",
   
}
#Hacemos la imagen en 64,64,3

class PythonPredictor:

    def __init__(self, config):
      print("[INFO] cargando el modelo entrenado")
      self.model = models.load_model(args["model"])
        
    def predict(self, payload):

        # Obtener la imagen por POST
        img = Image.open(payload["image"].file)
        print("[SIZE]",img.size)
        img= img.resize((64,64))
        print("[RESIZE]",img.size)
        img_tensor = np.array(img)
        img_tensor = np.expand_dims(img_tensor,axis=0)
        print("[SHAPE]",img_tensor.shape)
        img_tensor = img_tensor/255

        resultado =self.model.predict(img_tensor)
        print("[Resultado]",resultado)
        resultado = np.round(resultado[0][0])
        print("resultado redondeado" , resultado)

        valor = "Perro"
        if resultado == 0:
            valor= "Gato"
        res = {"resultado": valor}

        return json.dumps(res)

