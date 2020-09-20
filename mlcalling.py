import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import train_test_split


def mlcall(disarr):
    df = pd.read_csv("Training.csv")
    X, y = df[['receiving_blood_transfusion', 'red_sore_around_nose',
               'abnormal_menstruation', 'continuous_sneezing', 'breathlessness',
               'blackheads', 'shivering', 'dizziness', 'back_pain', 'unsteadiness',
               'yellow_crust_ooze', 'muscle_weakness', 'loss_of_balance', 'chills',
               'ulcers_on_tongue', 'stomach_bleeding', 'lack_of_concentration', 'coma',
               'neck_pain', 'weakness_of_one_body_side', 'diarrhoea',
               'receiving_unsterile_injections', 'headache', 'family_history',
               'fast_heart_rate', 'pain_behind_the_eyes', 'sweating', 'mucoid_sputum',
               'spotting_ urination', 'sunken_eyes', 'dischromic _patches', 'nausea',
               'dehydration', 'loss_of_appetite', 'abdominal_pain', 'stomach_pain',
               'yellowish_skin', 'altered_sensorium', 'chest_pain', 'muscle_wasting',
               'vomiting', 'mild_fever', 'high_fever', 'red_spots_over_body',
               'dark_urine', 'itching', 'yellowing_of_eyes', 'fatigue', 'joint_pain',
               'muscle_pain']], df.iloc[:, -1]
    X = X.to_numpy()
    y = y.to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)
    classifier1 = SVC(kernel="rbf")
    classifier1.fit(X_train, y_train)
    # classifier1.predict(X_test)
    d = str(classifier1.predict([disarr]))
    return d
