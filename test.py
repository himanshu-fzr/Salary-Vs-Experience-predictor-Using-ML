import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import r2_score, mean_absolute_error

#Load model and data
with open("model.pkl" ,"rb") as f:

    model=pickle.load(f)

df= pd.read_csv("Salary_data.csv")
x=df[["YearsExperience"]]
y=df["Salary"]

# Make Predictions
predictions =model.predict(x)

#Calculate Metrics
r2= r2_score(y, predictions)
mae = mean_absolute_error(y, predictions)

print(f"R^2 Score: { r2:.3f}")
print(f"MAE: ${mae: .2f}")