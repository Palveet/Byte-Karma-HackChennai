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

    # << << << < HEAD
    symptoms = ['receiving_blood_transfusion',
                'red_sore_around_nose',
                'abnormal_menstruation',
                'continuous_sneezing',
                'breathlessness',
                'blackheads',
                'shivering',
                'dizziness',
                'back_pain',
                'unsteadiness',
                'yellow_crust_ooze',
                'muscle_weakness',
                'loss_of_balance',
                'chills',
                'ulcers_on_tongue',
                'stomach_bleeding',
                'lack_of_concentration',
                'coma',
                'neck_pain',
                'weakness_of_one_body_side',
                'diarrhoea',
                'receiving_unsterile_injections',
                'headache',
                'family_history',
                'fast_heart_rate',
                'pain_behind_the_eyes',
                'sweating',
                'mucoid_sputum',
                'spotting_ urination',
                'sunken_eyes',
                'dischromic _patches',
                'nausea',
                'dehydration',
                'loss_of_appetite',
                'abdominal_pain',
                'stomach_pain'
                'yellowish_skin',
                'altered_sensorium',
                'chest_pain',
                'muscle_wasting',
                'vomiting',
                'mild_fever',
                'high_fever',
                'red_spots_over_body',
                'dark_urine',
                'itching',
                'yellowing_of_eyes',
                'fatigue',
                'joint_pain',
                'muscle_pain']

    #   symptoms = ['Sym A', 'Sym B', 'Sym C', 'Sym D']

    data = {
        "symptoms": symptoms
    }
    return json.dumps(data)


app.run()
