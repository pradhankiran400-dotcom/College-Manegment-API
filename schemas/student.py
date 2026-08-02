from pydantic import BaseModel

class Student_request(BaseModel):
    id: int
    name: str
    age: int
    branch: str


class Student_response(BaseModel):
    name: str
    age: int
    branch: str

