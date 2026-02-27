from pydantic import BaseModel
from typing import List


class JobRequest(BaseModel):
    job_description: str


class JobResponse(BaseModel):
    skills: List[str]


class JobOut(BaseModel):
    id: int
    job_title: str
    skills_extracted: List[str]