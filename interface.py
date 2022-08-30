import json
from flask import Flask, jsonify, render_template, request
import config
from project_app.utils import InsurenceUsa

app = Flask(__name__)

##########################################################################
@app.route('/') 
def hello_flask():
    print("Welcome to Flask")
    # return render_template("home.html")
    return 'Hello Python'

##########################################################################

@app.route('/predict_charges')
def get_insurence_charges():
    age = 80
    sex = 'female'
    bmi = 30.7
    children = 3
    smoker = 'yes'
    region = 'southeast'

    ins_usa = InsurenceUsa(age,sex,bmi,children,smoker,region)
    charges = ins_usa.get_predicted_charges()
    
    return jsonify({"Result":f"Predicted Insurance Charges are : {charges}"})

if __name__ == "__main__":
    app.run() 