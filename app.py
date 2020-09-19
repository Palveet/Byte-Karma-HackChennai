from flask import Flask, render_template, request
import json
from pharmnearme import searchparams

app = Flask(__name__)

# localhost:5000/


@app.route('/', methods=['GET'])
def hello():
    return render_template('about.html')


@app.route('/api/enter', methods=['GET'])
def hello_world():
    return render_template('index.html')

# localhost:5000/api/disease


@app.route('/nearmeshow', methods=['GET'])
def searching():
    return render_template('nearme.html')


@app.route('/nearmerun', methods=['POST'])
def queryInput():
    req_data = str(request.get_data(['cityname']))

    return json.dumps(searchparams(req_data))

    # print(req_data)
    # return "True"


@app.route('/api/disease', methods=['POST'])
def getDisease():
    req_data = request.get_json()
    print(req_data['symptoms'])

    return "You have fever"


@app.route('/api/symptoms', methods=['GET'])
def getSymptoms():

    symptoms = ['Sym A', 'Sym B', 'Sym C','Sym D']
    data = {
        "symptoms": symptoms
    }
    return json.dumps(data)


app.run()
