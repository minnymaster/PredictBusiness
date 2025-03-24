from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    df = pd.DataFrame([data])
    df['Total_GPA'] = df['High_School_GPA'] + df['University_GPA']
    df['Total_Experience'] = df['Internships_Completed'] + df['Projects_Completed']
    df['Social_Skills'] = df['Soft_Skills_Score'] + df['Networking_Score']
    
    features = df[['Total_GPA', 'Total_Experience', 'Social_Skills']] 
    
    prediction = model.predict(features)
    
    return jsonify({'result': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
