import pickle
import json
import config
import numpy as np

# CREATING CLASS OF MEDICAL INSSURANCE :
# ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']

class MedicalInsurance():
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region
    
    def load_model(self):
        with open(config.JSON_FILE_PATH, "r") as file :
            self.json_data = json.load(file)

        with open(config.PICKLE_PATH, "rb") as f:
            self.model = pickle.load(f)


    def predict_insurence_charge(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.age
        test_array[1] = self.json_data["sex"][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.json_data["smoker"][self.smoker]
        region_idx = self.json_data["columns"].index(self.region)
        test_array[region_idx] = 1 

        predict_charges = self.model.predict([test_array])
        return predict_charges
 
        