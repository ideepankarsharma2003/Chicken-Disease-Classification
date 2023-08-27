import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load the model
        model = load_model(
            os.path.join("artifacts", "training", "model.h5")
        )

        # load the image
        img = image.load_img(self.filename, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        # predict the image
        pred = model.predict(img)
        result = np.argmax(pred, axis=1)
        print(result)


        if result[0]==1:
            pred= ("Healthy")
        else:
            pred= ("Coccidiosis")
        
        return [{"image": pred }]