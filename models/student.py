from sqlalchemy import Column, Integer, String,UniqueConstraint,ForeignKey
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(
    Integer,
    primary_key=True,
    autoincrement=True
                )
    name = Column(String, index=True)
    age = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))

    __table_args__=(
        UniqueConstraint('name', 'age', 'department_id', name='unique_student'),
    )