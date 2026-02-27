import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import pandas as pd
from app.database import SessionLocal
from app.models.jobs_model import JobOffer


def seed_skills_from_csv(csv_path: str):
    db = SessionLocal()

    try:
        df = pd.read_csv(csv_path)
        print(f"✓ CSV chargé : {len(df)} lignes")
        print(f"✓ Colonnes : {df.columns.tolist()}")

        count = 0
        errors = 0

        for _, row in df.iterrows():
            try:
                # extraire le role
                role = str(row["role"]).strip() if pd.notna(row["role"]) else "Unknown"

                # extraire les skills
                raw_skills = row["extracted_skills"]
                if pd.isna(raw_skills):
                    continue

                skills_list = json.loads(str(raw_skills).replace("'", '"'))

                if not skills_list:
                    continue

                job = JobOffer(
                    role=role,
                    skills_extracted=json.dumps(skills_list)
                )
                db.add(job)
                count += 1

            except Exception as e:
                errors += 1
                continue

        db.commit()
        print(f"✓ {count} entrées insérées en DB")
        if errors:
            print(f" {errors} lignes ignorées (erreur parsing)")

    except Exception as e:
        db.rollback()
        print(f" Erreur : {e}")
    finally:
        db.close()


if __name__ == "__main__":
    csv_path = Path(__file__).parent.parent / "data" / "merged.csv"
    seed_skills_from_csv(str(csv_path))