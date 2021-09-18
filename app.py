from class import Flask,jsonify,request
from classifier import get_predition 

app = Flask (__name__)

@app.route("/predict")