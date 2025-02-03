from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional
from datetime import date

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# SQLAlchemy model
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String(1), nullable=False)
    enrollment_date = Column(Date)


Base.metadata.create_all(bind=engine)


# Pydantic model
class StudentModel(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=3, max_length=50)
    age: int
    grade: str = Field(..., pattern="^[A-F]$")
    enrollment_date: Optional[date] = None


app = FastAPI()


@app.post("/students/", response_model=StudentModel)
def create_student(student: StudentModel):
    db = SessionLocal()
    new_student = Student(
        name=student.name,
        age=student.age,
        grade=student.grade,
        enrollment_date=student.enrollment_date
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()
    return new_student


@app.get("/students/{student_id}", response_model=StudentModel)
def read_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    db.close()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.put("/students/{student_id}", response_model=StudentModel)
def update_student(student_id: int, updated_student: StudentModel):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = updated_student.name
    student.age = updated_student.age
    student.grade = updated_student.grade
    student.enrollment_date = updated_student.enrollment_date
    db.commit()
    db.refresh(student)
    db.close()
    return student


@app.patch("/students/{student_id}")
def partial_update_student(student_id: int, updates: dict):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in updates.items():
        if hasattr(student, key):
            setattr(student, key, value)
    db.commit()
    db.refresh(student)
    db.close()
    return student


@app.get("/students/", response_model=List[StudentModel])
def list_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    db.close()
    return {"detail": "Student deleted successfully"}


@app.get("/students/search/", response_model=List[StudentModel])
def search_students(name: str):
    db = SessionLocal()
    students = db.query(Student).filter(Student.name.ilike(f"%{name}%")).all()
    db.close()
    return students
