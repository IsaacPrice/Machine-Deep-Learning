import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

dataFrame = pd.read_csv('carprices.csv')
dummies = pd.get_dummies(dataFrame.model)

merged = pd.concat([dataFrame, dummies],axis='columns')
final = merged.drop(['model', 'Mercedez Benz C class'], axis='columns')

X = final.drop('sell_price', axis='columns')
y = final.sell_price

model = LinearRegression()
model.fit(X,y)

with open('model_pickle','wb') as f:
    pickle.dump(model, f)

print(model.score(X,y))