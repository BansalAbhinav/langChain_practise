from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str = "abhi"
    age:Optional[int]= None
    email:EmailStr
    cgpa:float = Field(st=0,lt=10,default=4,description="this is a cgpa of student")


new_student = {'age':32,'email':"abc@gmail.com","cgpa":1 }    

student = Student(**new_student)

student_dict = dict(student)
student_json = student.model_dump_json()
print(student_dict)
print(student)
print(student_json)