import joblib
from pathlib import Path
import pandas as pd




BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ml" / "training_models" / "predict_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_salary(features):

    X = pd.DataFrame([features])
    prediction = model.predict(X)[0]

    return float(prediction)