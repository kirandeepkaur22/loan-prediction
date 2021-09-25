import pickle
import numpy
from flask import Flask, request, render_template

app = Flask(__name__)
loadedmodel = pickle.load(open('loan_data_set.pkl','rb'))

@app.route("/", methods = ['GET'])
def home():
    return render_template('index.html')
@app.route("/prediction", methods =['POST'])
def predict():
    Total_Income = float(request.form['Total_Income'])
    LoanAmount = float(request.form['LoanAmount'])
    LoanAmountTerm = float(request.form['LoanAmountTerm'])
    CreditHistory = request.form['CreditHistory']

    prediction = loadedmodel.predict([[Total_Income,LoanAmount,LoanAmountTerm,CreditHistory]])

    if prediction == [0]:
        prediction = 'Sorry your loan will not get approved.'
    else:
        prediction = 'Yay! Your loan will be approved.'
    return render_template('index.html', output = prediction )
    
#main function
if __name__ == "__main__":
    app.run(debug=True)
