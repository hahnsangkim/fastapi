from pydantic import BaseModel
import enum


class Role(enum.Enum):
    admin = "admin"
    personel = "personel"

class User(BaseModel):
    name: str
    password: str
    mail: str
    role: Role