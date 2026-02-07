from pydantic import BaseModel

class Usercreate(BaseModel):
    name: str
    email: str
    password: str