from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from prediction import PredictionPipeline


app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            ambient_temperature = float(request.form['ambient_temperature'])
            module_temperature = float(request.form['module_temperature'])
            irradiation = float(request.form['irradiation'])

            data = [ambient_temperature, module_temperature, irradiation]
            data = np.array(data).reshape(1,3)

            obj = PredictionPipeline()
            predict = obj.predict(data)
            
            print(str(predict))

            return render_template('index.html', predict = str(predict))

        except Exception as e:
            return 'Something is wrong: ${e}'




if __name__ == "__main__":
    app.run(debug=True)