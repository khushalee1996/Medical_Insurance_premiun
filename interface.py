from flask import Flask, jsonify, render_template, request
from medical_insurance.utils import MediInfo

app=Flask(__name__)
@app.route('/')
def home_api():
    print('This is my home api')
    return render_template('home.html')
    
######################################################
@app.route('/test')
def test():
    print('This is my home api')

    return "hello"
# ##########################################
@app.route("/pedict_premium")
def get_predict():
    param=request.form
    print("parameters :",param)
    age=eval(param['age'])
    sex=eval(param['sex'])
    bmi=eval(param['bmi'])
    children=eval(param['children'])
    smoker=eval(param['smoker'])
    region=eval(param['region'])
    m1=MediInfo(age, sex, bmi, children, smoker,region)
    premium=m1.get_predict()
    return jsonify({'predicted premium is :':{premium}})


if __name__=="__main__":
    app.run(host='0.0.0.0',port=2400)