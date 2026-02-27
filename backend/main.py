from fastapi import FastAPI, HTTPException
from backend.services.pedict_service import predict_salary
from backend.services.skills_model import run_ner_extraction, authenticate_client
from backend.schemas.extract_skills import JobRequest, JobResponse
from backend.schemas.predict_schema import UserRequest, UserResponse
from backend.database import Base, engine
from backend.models import users_model
from backend.schemas.extract_skills import JobRequest, JobResponse, JobOut
from typing import List
from backend.services.extract_skills import get_all_skills, get_jobs_by_skill, extract_skills_from_text



Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.post("/predict", response_model=UserResponse)
def predict(data: UserRequest):
    print(data)
    data = data.dict()
    salary = predict_salary(data)
 

    return {"salary": salary}


