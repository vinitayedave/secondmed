from operator import index
import pickle
import json
import numpy as np
import config 

class InsurenceUsa():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_' + region

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)   

    def get_predicted_charges(self):
        self.load_model()

        region_index = (self.json_data['columns']).index(self.region)
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.age
        test_array[1] = self.json_data['sex'][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data['smoker'][self.smoker]
        test_array[region_index] = 1
        predicted_charges = self.model.predict([test_array])
        return predicted_charges

        print("Test array :",test_array)

if __name__ == "__main__":
    age = 19.0
    sex = 'female'
    bmi = 27.9
    children = 3
    smoker = 'no'
    region = 'southwest'

    ins_usa = InsurenceUsa(age,sex,bmi,children,smoker,region)
    ins_usa.get_predicted_charges()
