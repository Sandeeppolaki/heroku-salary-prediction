from flask import Flask, render_template, request
app = Flask(__name__)    # behind the scene -> __name__ cahnges to mani.py
import joblib
model = joblib.load('hiring_model.pkl')
@app.route('/')
def welcome():
    return render_template('bas1.html')

@app.route('/predict', methods = ['POST'])
def predict():
    exp = request.form.get('experience')
    score = request.form.get('test_score')
    interview_score = request.form.get('interview_score')
    predictions = model.predict([[int(exp), int(score), int(interview_score)]])
    output = round(predictions[0],2)
    return render_template('bas1.html' , prediction_text = f"Employee Salary will be $ {output}")


app.run(debug = True)     
# debug will keep on updating in server, any new 
# function added will immediately updated
#  in DeprecationWarning