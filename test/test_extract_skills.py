import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)




def test_get_skills():
    response = client.get("/skills")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# test jobs list

def test_get_jobs():
    response = client.get("/jobs")

    assert response.status_code == 200


# test jobs by skill

def test_jobs_by_skill():
    response = client.get("/jobs_by_skill/python")

    assert response.status_code in [200, 404]