from fastapi import FastAPI, HTTPException, Depends
from app.services.predict_service import predict_salary
from app.schemas.predict_schema import PredictRequest, PredictResponse
from app.database import Base, engine, get_db
from app.models import jobs_model, users_model
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserResponse, UserVerify
from app.models.users_model import User
from app.auth import create_token, verify_password, verify_token, hache_password
from app.schemas.skills_schema import JobRequest, JobResponse, JobOut
from typing import List
from app.services.extract_skills import get_all_skills, get_jobs_by_skill
from fastapi.middleware.cors import CORSMiddleware
from app.models.jobs_model import JobOffer

from app.telemetry import setup_telemetry

Base.metadata.create_all(bind=engine)

app = FastAPI()

# setup Telemetry
setup_telemetry(app, engine)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# creation d'un username :
@app.post("/register", response_model=UserResponse)
def create_user(user:UserCreate, db: Session=Depends(get_db)):
    exist = db.query(User).filter(User.username == user.username).first()

    if exist:
        raise HTTPException(status_code=400, detail= "username existe deja")
    
    # haching password
    hashed_pwd = hache_password(user.password)
    
    new_user = User(username=user.username, password=hashed_pwd, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user




# verifier l'identifiant et encoder token
@app.post("/login")
def login(user:UserVerify, db: Session=Depends(get_db)):

    db_user = db.query(User).filter(
        User.username == user.username
        ).first()
    
    if not db_user or not verify_password(user.password,db_user.password):
        raise HTTPException(status_code=400, detail="username or password incorect")
    
    token = create_token(db_user.username)

    return {"token" : token}




# predict salary
@app.post("/predict", response_model=PredictResponse)
def predict(data: PredictRequest):
    print(data)
    data = data.dict()
    salary = predict_salary(data)

    return {"salary": salary}



# skills list
@app.get("/skills", response_model=list[str])
def list_skills(db: Session = Depends(get_db)):
    return get_all_skills(db)


@app.get("/jobs")
def jobs(db: Session = Depends(get_db)):
    return db.query(JobOffer).all()



# jobs list
@app.get("/jobs_by_skill/{skill}")
def jobs_by_skill(skill: str, db: Session = Depends(get_db)):
    result = get_jobs_by_skill(db, skill)

    if not result:
        raise HTTPException(status_code=404, detail="No jobs found")

    return result
