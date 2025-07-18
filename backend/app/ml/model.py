# app/model.py
# Author Ilija - password strength ML trainer

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model():
    df = pd.read_csv('data.csv', dtype={'password': str, 'strength': int}, low_memory=False)
    # df = pd.read_csv('data.csv')

    # df = df.dropna(subset=['password', 'strength'])#drop every values that are empty

    df = df.dropna(subset=['password', 'strength'])
    df = df[df['password'].str.strip() != '']


    X = df['password'].astype(str) 
    y = df['strength'].astype(int)  # 0,1,2

    vec = TfidfVectorizer(analyzer='char')  # char-level za passworde
    X_vec = vec.fit_transform(X)

    model = RandomForestClassifier()
    model.fit(X_vec, y)

    os.makedirs('app', exist_ok=True)
    joblib.dump(model, 'app/model.pkl')
    joblib.dump(vec, 'app/vectorizer.pkl')

if __name__ == '__main__':
    train_model()
