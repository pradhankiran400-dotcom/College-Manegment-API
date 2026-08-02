from pydantic import BaseModel, ConfigDict


class StudentRequest(BaseModel):
    name: str
    age: int
    branch: str

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    branch: str

    model_config = ConfigDict(from_attributes=True)