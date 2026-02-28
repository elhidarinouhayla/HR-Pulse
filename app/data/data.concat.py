from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

df_skills = pd.read_csv(BASE_DIR / "processed" / "skills_data.csv")
df_jobs = pd.read_csv(BASE_DIR / "processed" / "jobs_data_cleaned.csv")

df_jobs["extracted_skills"] = df_skills["extracted_skills"]

df_jobs.to_csv(BASE_DIR / "merged.csv", index=False)