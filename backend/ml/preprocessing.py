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



def categorize_ownership(ownership):
    if ownership in ["-1", "Unknown", "Other Organization"]:
        return "Unknown"
    
    if "Private" in ownership or "Subsidiary" in ownership:
        return "Private"
    
    if "Public" in ownership:
        return "Public"
    
    if "Nonprofit" in ownership:
        return "Nonprofit"
    
    if "Government" in ownership:
        return "Government"
    
    if "College" in ownership:
        return "Education"
    
    if "Hospital" in ownership:
        return "Healthcare"
    
    if ownership in ["Self-employed", "Contract"]:
        return "Self-employed"
    
    return "Unknown"



# regrouper Size en categories

def categorize_size(size):
    if size in ["Unknown", "-1"]:
        return "Unknown"
    
    if "1 to 50" in size or "51 to 200" in size:
        return "Small"
    
    if "201 to 500" in size or "501 to 1000" in size:
        return "Medium"
    
    if "1001 to 5000" in size:
        return "Large"
    
    if "5001 to 10000" in size or "10000+" in size:
        return "Enterprise"
    
    return "Unknown"
    
    
# transformer Revenue en categorie

def categorize_revenue(revenue):
    if revenue in ["Unknown / Non-Applicable", "-1"]:
        return "Unknown"
    
    if "Less than $1 million" in revenue:
        return "Very Small"
    
    if "$1 to $5 million" in revenue:
        return "Very Small"
    
    if "$5 to $50 million" in revenue:
        return "Small"
    
    if "$50 to $500 million" in revenue:
        return "Medium"
    
    if "$500 million to $1 billion" in revenue:
        return "Large"
    
    if "billion" in revenue:
        return "Enterprise"
    
    return "Unknown"
