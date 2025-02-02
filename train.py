import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# parameter
output_file = 'model.bin'

# data preparation

data = "https://raw.githubusercontent.com/bankymondial/Placement-Prediction/refs/heads/main/placementdata.csv"
df = pd.read_csv(data)


df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('/', '')
df['placementstatus'] = df['placementstatus'].map({'NotPlaced': 0, 'Placed': 1})


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)


categorical = ['extracurricularactivities', 'placementtraining']
numerical = ['cgpa', 'aptitudetestscore', 'ssc_marks', 'hsc_marks', 
             'internships', 'projects', 'workshopscertifications', 'softskillsrating']

# training

def train(df_train, y_train):
    dicts = df_train[categorical + numerical].to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = LogisticRegression(solver='liblinear', random_state=1)
    model.fit(X_train, y_train)
    
    return dv, model

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

# training the final model

dv, model = train(df_full_train, df_full_train.placementstatus.values)
y_pred = predict(df_test, dv, model)

y_test = df_test.placementstatus.values
auc = roc_auc_score(y_test, y_pred)
auc

print(f'auc={auc}')

# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)
   
print(f'the model is saved to {output_file}')