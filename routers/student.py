from fastapi import APIRouter, HTTPException
from schemas.student import Student_request, Student_response
import json

router = APIRouter()


def read_students():
    with open("data/students.json", "r") as file:
        return json.load(file)


def save_students(data):
    with open("data/students.json", "w") as file:
        json.dump(data, file, indent=4)


@router.get("/{student_id}")
def get_student(student_id: int):

    for student in read_students():

        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@router.post(
    "/",
    response_model=Student_response
)
def add_student(student: Student_request):

    students = read_students()

    for stud in students:

        if stud["id"] == student.id:

            raise HTTPException(
                status_code=400,
                detail="Student already exists"
            )

    students.append(student.model_dump())

    save_students(students)

    return student


@router.put("/{student_id}")
def update_student(student_id: int, branch: str):

    students = read_students()

    for student in students:

        if student["id"] == student_id:

            student["branch"] = branch

            save_students(students)

            return {
                "message": "Updated"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@router.delete("/{student_id}")
def delete_student(student_id: int):

    students = read_students()

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            save_students(students)

            return {
                "message": "Deleted Successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
    