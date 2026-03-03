import json
import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).parent.parent.parent))

from app.database import SessionLocal
from app.models.jobs_model import JobOffer


def seed_skills_from_csv(csv_path):
    db = SessionLocal()

    # lire CSV
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():

        # recuperer le role
        role = row["role"]
        if pd.isna(role):
            role = "Unknown"
        else:
            role = str(role).strip()

        # Recuperer les skills
        raw_skills = row["extracted_skills"]

        if pd.isna(raw_skills):
            continue

        skills_list = json.loads(str(raw_skills).replace("'", '"'))

        if len(skills_list) == 0:
            continue

        job = JobOffer(
            role=role,
            skills_extracted=json.dumps(skills_list)
        )

        db.add(job)

  
    db.commit()
    db.close()


if __name__ == "__main__":
    csv_path = Path(__file__).parent.parent / "data" / "merged.csv"
    seed_skills_from_csv(str(csv_path))