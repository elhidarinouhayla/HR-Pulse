from fastapi import FastAPI
from predictor import predict_salary

app = FastAPI()

Base.metadata.create_all(bind=engine)


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









@app.post("/predict")
def predict(data: dict):
    features = [
        data["rating"]
    ]
    salary = predict_salary(features)
    return {"predicted_salary": salary}