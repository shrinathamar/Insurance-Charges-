
from flask import Flask, render_template, jsonify, request
from utils import MedicalInsurance
import pandas as pd
import config



app = Flask(__name__)

@app.route("/")
def project():
    return render_template("index.html")

@app.route("/predict_charge", methods=["POST"])
def get_medical_charges():
    

    data = request.form

    age = int(data["age"])
    sex = (data["sex"])
    bmi = eval(data["bmi"])
    children = int(data["children"])
    smoker = (data["smoker"])
    region = (data["region"])

    med_ch = MedicalInsurance(age=age, sex=sex, bmi=bmi, children=children, smoker=smoker, region=region)
    charge = med_ch.predict_insurence_charge()
  
    return render_template("result.html", price=charge, age=age, sex=sex, bmi=bmi, children=children, smoker=smoker, region=region)
    # return "hello"

# age = 40
# sex = "male"
# bmi = 32
# children = 2
# smoker = "no"
# region = "northwest"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUM1)