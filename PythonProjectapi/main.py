from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class Student(BaseModel):
    id:str
    name:str
    age:int
students=[]
@app.get("/students", response_model=list[Student])
async def read_students():
    return students
@app.get("/students/{s_id}", response_model=Student)
async def read_student(s_id:str):
    for s in students:
        if s.id==s_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found.")
@app.post("/students", response_model=Student)
async def create_student(s:Student):
    for i in students:
        if i.id==s.id:
            raise HTTPException(status_code=400, detail="ID already exists.")
    students.append(s)
    return s
@app.put("/students/{s_id}", response_model=Student)
async def update_student(s_id:str, student:Student):
    for i, s in enumerate(students):
        if s.id==s_id:
            students[i] = student
            return student
    raise HTTPException(status_code=404, detail="Student not found.")
@app.delete("/students/{s_id}")
async def delete_student(s_id:str):
    for i, s in enumerate(students):
        if s.id==s_id:
            del students[i]
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found.")
