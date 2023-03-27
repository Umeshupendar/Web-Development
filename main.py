from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method=="POST":
        bedrooms = int(request.form.get('bedrooms'))
        doublebedrooms = int(request.form.get('doublebedrooms'))
        floors = int(request.form.get('floors'))
        yr_built = int(request.form.get('yr_built'))
        data = model.predict([[bedrooms, doublebedrooms, floors, yr_built]])[0][0]

        return render_template('result.html', bedrooms=bedrooms,
                               doublebedrooms=doublebedrooms, floors=floors,
                               yr_built=yr_built, data=int(data))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)