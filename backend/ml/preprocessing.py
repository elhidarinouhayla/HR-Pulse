import re
import pandas as pd
import numpy as np

def clean_salary(salary_str):
    if pd.isna(salary_str):
        return None

    salary_str = salary_str.split("(")[0]
    salary_str = salary_str.replace("$", "").replace("K", "")

    numbers = re.findall(r"\d+", salary_str)

    if len(numbers) >= 2:
        low = int(numbers[0])
        high = int(numbers[1])
        return ((low + high) / 2) * 1000

    return None




# nettoyage du texte

def job_title(title):

    title = title.lower()
    title = re.sub(r'[^a-zA-Z ]', '', title)  # enlever chiffres et symboles
    title = title.strip()

    return title



# extraire le niveau d’experience

def extract_seniority(title):

    if not isinstance(title, str):
        return "Mid"
    
    if "senior" in title or "sr" in title:
        return "Senior"
    elif "junior" in title or "jr" in title:
        return "Junior"
    elif "lead" in title:
        return "Lead"
    elif "principal" in title:
        return "Principal"
    else:
        return "Mid"
    


# regroupement des roles 

def extract_role(title):

    if not isinstance(title, str):
        return "Other"

    if "data scientist" in title:
        return "Data Scientist"
    
    elif "data analyst" in title:
        return "Data Analyst"
    
    elif "machine learning" in title:
        return "ML Engineer"
    
    elif "data engineer" in title:
        return "Data Engineer"
    
    else:
        return "other"


# remplacer les valeurs du Revenue par la mediane

def clean_revenue(value):
    if not isinstance(value, str):
        return np.nan

    if "Unknown" in value or "Non-Applicable" in value:
        return np.nan

    value = value.lower()

    numbers = re.findall(r"[\d\.]+", value)

    if len(numbers) == 2:
        low, high = map(float, numbers)

        if "billion" in value:
            low *= 1000
            high *= 1000

        return (low + high) / 2

    return np.nan
