import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)




def test_predict_salary():
    response = client.post(
        "/predict",
        json={
            "JobDescription": "machine learning engineer",
            "location": "morocco",
            "role": "engineer",
            "ownership_category": "private",
            "Industry": "tech",
            "Sector": "AI"
        }
    )

    assert response.status_code == 200
    assert "salary" in response.json()