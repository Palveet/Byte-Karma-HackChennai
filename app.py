from flask import Flask, render_template, request
app = Flask(__name__)

# localhost:5000/


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

# localhost:5000/api/disease


@app.route('/api/disease', methods=['POST'])
def getDisease():
    req_data = request.get_json()
    print(req_data)
    return "You have fever"


app.run()
