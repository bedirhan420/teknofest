import pandas as pd 
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("data.csv")

X = data.drop(columns=['ExcersiseType'])
y = data['ExcersiseType']

X = pd.get_dummies(X)
print(X)

model = SVC(kernel='linear')

model.fit(X, y)

import joblib
joblib.dump(model, 'exercise_model.pkl')
