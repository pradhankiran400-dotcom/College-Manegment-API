from sqlalchemy import Column, Integer, String,UniqueConstraint
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
    branch = Column(String)

    __table_args__=(
        UniqueConstraint('name', 'age', 'branch', name='unique_student'),
    )