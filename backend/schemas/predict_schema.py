from pydantic import BaseModel


class PredictRequest(BaseModel):

    JobDescription: str
    location: str
    role: str
    ownership_category: str
    Industry: str
    Sector: str
        


class PredictResponse(BaseModel):
    salary : float