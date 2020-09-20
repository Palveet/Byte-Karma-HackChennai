from flask import Flask, render_template, request, redirect, url_for
import json
from pharmnearme import searchparams
from hospnearme import searchhosp
from databasecomm import databaseadd
from mlcalling import mlcall

app = Flask(__name__)
name_inp = ""
age_inp = ""
gen_imp = ""
dis = ""

# localhost:5000/


@app.route('/', methods=['GET'])
def hello():
    print("Reached here")
    return render_template('about.html')


@app.route('/main.css', methods=['GET'])
def hell():
    return render_template('main.css')


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
            names = searchparams(cityName)
            res = True
            # return (json.dumps(searchparams(cityName)))
        elif choice == 'Hospital':
            cityName = req_data['cityname']
            names = searchhosp(cityName)
            res = True
            # return (json.dumps(searchhosp(cityName)))
        return render_template('nearme.html', res=res, names=names)


@app.route('/api/disease', methods=['POST'])
def getDisease():
    req_data = request.get_json()
    # print(req_data['symptoms'])
    dis = mlcall(req_data['symptoms'])
    print(dis[0])
    dis = str(dis[0])
    databaseadd(name_inp, gen_imp, age_inp, dis)
    return dis


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
    print(name_inp)
    data = {
        "symptoms": symptoms,
        "name": name_inp
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
        global name_inp
        name_inp = str(req_data['name'])
        global gen_imp
        gen_imp = str(req_data['gen'])
        global age_inp
        age_inp = str(req_data['age'])
        print(name_inp, gen_imp, age_inp)
        return redirect("/api/enter", code=302)


@app.route('/getname', methods=['GET'])
def getName():

    return name_inp


app.run()
