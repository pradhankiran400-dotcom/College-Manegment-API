from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from database import get_db
from models.student import Student
from schemas import student
from schemas.student import StudentRequest, StudentResponse
import json

router = APIRouter()


# def read_students():
#     with open("data/students.json", "r") as file:
#         return json.load(file)


# def save_students(data):
#     with open("data/students.json", "w") as file:
#         json.dump(data, file, indent=4)

@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):

    students = db.query(Student).all()

    return students

@router.get("/{student_id}",response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.post("/", response_model=StudentResponse)
def add_student(
    student: StudentRequest,
    db: Session = Depends(get_db)
):

    existing_student = (
        db.query(Student)
        .filter(Student.name == student.name, Student.age == student.age, Student.branch == student.branch)
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student already exists"
        )

    new_student = Student(
        name=student.name,
        age=student.age,
        branch=student.branch
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int,
                    student_data: StudentRequest,
                     db: Session = Depends(get_db)):
    db_student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db_student.name = student_data.name
    db_student.age = student_data.age
    db_student.branch = student_data.branch

    db.commit()
    db.refresh(db_student)

    return db_student


@router.delete("/{student_id}")
def delete_student(student_id: int,
                     db: Session = Depends(get_db)):
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}

    