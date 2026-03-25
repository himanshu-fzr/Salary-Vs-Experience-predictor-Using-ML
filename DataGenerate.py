import pandas as pd
import numpy as np

# Generate Synthetic data
np.random.seed(42)
year_exp=np.random.uniform(0,10,100)
salary=20000 + 5000 * year_exp + np.random.normal(0,10000,100)

#Create DataFrame and save to CSV
df=pd.DataFrame({"YearsExperience": year_exp, "Salary": salary})
df.to_csv("Salary_data.csv",index=False)
print("Dataset generated and saved as salary_data.csv")