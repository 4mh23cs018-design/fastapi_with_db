from pydantic import BaseModel

class User_Schema(BaseModel):
    name: str
    email: str
    password: str