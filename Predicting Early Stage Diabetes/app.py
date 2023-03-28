# an object of WSGI application
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

import numpy as np

app = Flask(__name__, template_folder="templates")   # Flask constructor

#Loading Models:
#Loading Models:
with open("C:\Users\hp\OneDrive\Desktop\Front-End-Diabetes-GDSC-CIT\Front-End-Diabetes-GDSC-CIT\models\dtree.pkl", "rb") as file:
        model = pickle.load(file)
print("Model loaded")

@app.route('/', methods=['GET'])
@app.route('/home')
@cross_origin()                 # a web page hosted on one domain cannot make requests to a web server hosted on a different domain, unless the server explicitly allows it.
def home():
     return render_template("index.html", title="Home")

@app.route('/about')
def about():
     return render_template("about.html", title="About")

@app.route('/author')
def author():
     return render_template("author.html", title="Author")

@app.route('/predict',methods=['GET', 'POST'])
@cross_origin()
def predict():
     if request.method == "POST":
        #Name:
        name = request.form['tname']

		# Age
        age = request.form['nage']

		# Gender
        gender = float(request.form['tgender'])

		# Polyuria
        polyuria = float(request.form['tpolyuria'])

        # Polydipsia
        polydipsia = float(request.form['tpolydipsia'])

		# Weight-Loss
        wloss = float(request.form['twloss'])

		# Weakness
        weak = float(request.form['tweak'])

		# Polyphagia
        polyphagia = float(request.form['tpolyphagia'])

		# Genital
        genital = float(request.form['tgenital'])

		# Visual B
        visualb = float(request.form['tvisualb'])

		# Itiching
        itch = float(request.form['titch'])

		# Irritabile
        irrit = float(request.form['tirrit'])

		# Heal
        heal = float(request.form['theal'])

		# Paresis
        paresis = float(request.form['tparesis'])

		# Muscle
        muscle = float(request.form['tmuscle'])

		# Alopecia
        alopecia = float(request.form['talopecia'])

		# Obesity
        obesity = float(request.form['tobesity'])
        
        #Store-Array
        input_lst = [[age, gender, polyuria, polydipsia, wloss, weak, polyphagia, genital, visualb, itch, irrit, heal, paresis, muscle, alopecia, obesity]]
		
		# import numpy as np
        input_array = np.array(input_lst)
        input_array = input_array.reshape(1, -1) # reshape to 2D array with 1 sample and n features
        pred = model.predict(input_array)

        output = pred
        if output == 1:
            #  return "Yes"
            return render_template("result2.html", title="Output", name=name)
        else:
            #  return "No"
            return render_template("result1.html", title="Output", name=name)        

     return render_template("predict.html", title="Predictions")

if __name__=='__main__':
    app.run(debug = True)