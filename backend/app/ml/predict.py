# app/predict.py

import joblib

model = joblib.load('app/model.pkl')
vectorizer = joblib.load('app/vectorizer.pkl')

def predict(password):
    vec = vectorizer.transform([password])
    result = model.predict(vec)[0]
    return int(result)  # vraca 0,1,2
