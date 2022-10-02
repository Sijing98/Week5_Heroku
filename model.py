import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('demand.csv')

X = dataset.iloc[:, 2:6]
Y = dataset.iloc[:, 1]  # predicted column

# build regression model
regressor = LinearRegression()
regressor.fit(X, Y)

# save the simple model
pickle.dump(regressor, open('model.pkl','wb'))

# load the simple model
model = pickle.load(open('model.pkl','rb'))

print(model.predict([[63, 1610000, 16200, 200]]))

