from sqlmodel import SQLModel, Field, Column, VARCHAR
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

    
class CreateUser(SQLModel):
    name:str
    email: EmailStr =Field(sa_column=Column("email", VARCHAR , unique= True,  index =True ), description="Email of the passenger")
    password: PhoneNumber = Field (description="Phone number of the passenger" , title ="Phone Number")
    age: int 
    
class User(CreateUser ,  table = True):
    id: int | None = Field(default=None, primary_key=True)