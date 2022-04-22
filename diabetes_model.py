import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle

# LOADING THE DATASET INTO A VARIABLE
df = pd.read_csv("diabetes.csv")

#ASSIGNING DATA TO MY DEPENDENT AND INDEPENDENT VARIABLE
X = df.drop(columns =['Outcome'])
y = df['Outcome']

#SPLITTING THE DATASET INTO TRAINING AND TEST
X_train, X_test, y_train, y_test = train_test_split(X , y, test_size =0.2)

#USING RANDOM FOREST CLASSIFIER MODEL TO PREDICT
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
#Rfc = model.predict(X_test)

#score = accuracy_score(y_test, Rfc)
#print(score)

# Saving model to disk

pickle.dump(model, open('Diabetes_model.pkl','wb'))

# Loading model to compare the results
# model = pickle.load(open('D_model.pkl','rb'))
# print(model.predict([[	13,	126	,90,	0,	0	,43.4,	0.583,	42
# ]]))