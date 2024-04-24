from flask import Flask,render_template,jsonify,request
from src.pipeline.prediction_pipeline import PredictPipeline,CustomData

app=Flask(__name__)

@app.route('/')

def home_page():
    return render_template("index.html")

@app.route("/predict",method=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("form.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)