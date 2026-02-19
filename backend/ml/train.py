import pandas as pd
from preprocessing import clean_salary

df = pd.read_csv("../data/raw/jobs_data.csv")

df["salary_clean"] = df["Salary Estimate"].apply(clean_salary)
