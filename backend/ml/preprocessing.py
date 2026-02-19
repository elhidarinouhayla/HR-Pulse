import re
import pandas as pd

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
