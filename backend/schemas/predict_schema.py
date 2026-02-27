from pydantic import BaseModel


class UserRequest(BaseModel):

    JobDescription: str
    location: str
    role: str
    ownership_category: str
    Industry: str
    Sector: str
        


class UserResponse(BaseModel):
    salary : float