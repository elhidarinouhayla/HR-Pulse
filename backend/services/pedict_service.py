import joblib

def load_model():
    model = joblib.load("../ml/training_models/predict_model.pkl")


def predict_salary(df):
    model = load_model()
    prediction = model.predict([df])
    result = prediction[0]
    
    return result