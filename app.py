from flask import Flask, render_template, request, redirect
import json
from pharmnearme import searchparams
from hospnearme import searchhosp

app = Flask(__name__)

# localhost:5000/


@app.route('/', methods=['GET'])
def hello():
    return render_template('about.html')


@app.route('/api/enter', methods=['GET'])
def hello_world():
    return render_template('index.html')

# localhost:5000/api/disease


@app.route('/nearmeshow', methods=['GET', 'POST'])
def searching():
    if request.method == 'GET':
        return render_template('nearme.html')
    elif request.method == 'POST':
        req_data = request.form
        choice = req_data['choice']
        print(choice)
        if choice == 'Pharmacy':
            cityName = req_data['cityname']
            return str(json.dumps(searchparams(cityName)))
        elif choice == 'Hospital':
            cityName = req_data['cityname']
            return str(json.dumps(searchhosp(cityName)))


@app.route('/api/disease', methods=['POST'])
def getDisease():
    req_data = request.get_json()
    print(req_data['symptoms'])

    return "You have fever"


@app.route('/api/symptoms', methods=['GET'])
def getSymptoms():

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
                'stomach_pain',
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

    data = {
        "symptoms": symptoms
    }
    return json.dumps(data)


@app.route('/per_det', methods=['GET', 'POST'])
def getPerDet():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        # data = request.get_data(['name'])
        # print(data)
        req_data = request.form
        print(req_data)
        name_inp = str(req_data['name'])
        gen_inp = str(req_data['gen'])
        age_inp = str(req_data['age'])
        print(name_inp, gen_inp, age_inp)
        return redirect("/api/enter", code=302)


app.run()
