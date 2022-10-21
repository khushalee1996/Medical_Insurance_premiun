import json
import pickle

import numpy as np


class MediInfo():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region
    def load_model(self):
        with open('linear_model.pkl','rb') as f:
            self.model=pickle.load(f)
        with open('labled_data.json','r') as f:
            self.json_data=json.load(f)
    def get_premium(self):
        self.load_model()
        region_index=self.json_data['columns'].index(self.region)
        test_array=np.zeros(len(self.json_data['columns']))
        test_array[0]=self.age
        test_array[1]=self.json_data['sex'][self.sex]
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.json_data['smoker'][self.smoker]
        test_array[region_index]=1
        
        print('test array :',test_array)
        premium=self.model.predict([test_array])[0]
        print("predicted charges :",premium)
        return premium
    
    
if __name__=="__main__":
    
    age=21
    sex='male'
    bmi=60
    children=2
    smoker='yes'
    region='southeast'
    param=MediInfo(age,sex,bmi,children,smoker,region)
    param.get_premium()

