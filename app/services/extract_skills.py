import json
from app.models.jobs_model import JobOffer
from sqlalchemy.orm import Session


def get_all_skills(db: Session):
    skills_set = set()

    jobs = db.query(JobOffer.skills_extracted).all()
    for (skills_text,) in jobs:
        try:
            skills_list = json.loads(skills_text)
            for skill in skills_list:
                skills_set.add(skill.lower().strip())
        except:
            continue

    return sorted(list(skills_set))


def get_jobs_by_skill(db: Session, skill: str):
    skill = skill.lower()

    jobs = db.query(JobOffer).all()

    filtered = []

    for job in jobs:
        try:
            skills_list = json.loads(job.skills_extracted)

            if any(skill in s.lower() for s in skills_list):
                filtered.append(job)

        except:
            continue

    return filtered