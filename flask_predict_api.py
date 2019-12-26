# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:00:14 2019

@author: Omkar R
"""

import pickle
from flask import  Flask,request
from flasgger import Swagger
import pandas as pd
import numpy as np

with open('C:/Users/lenovo pc/Desktop/Flask/rf.pkl','rb') as model_file:
    model=pickle.load(model_file)


app=Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def defa():
    print('Its Running')
    return ''


@app.route('/predict')
def predict_iris():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length=request.args.get("s_length")
    s_width=request.args.get("s_width")
    p_length=request.args.get("p_length")
    p_width=request.args.get("p_width")
    prediction=model.predict(np.array([[s_length,s_width,p_length,p_width]]))
    
    return str(prediction)

@app.route('/predict_file',methods=['POST'])
def predict_iris_file():    
    
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data=pd.read_csv(request.files.get('input_file'),header=None)
    prediction=model.predict(input_data)
    return str(list(prediction))


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
    
    
    