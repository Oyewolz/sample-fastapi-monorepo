
from sqlmodel import Field, SQLModel
from ..base_entity import BaseEntity

class FTUser(BaseEntity, table=True):
    first_name: str
    last_name: str
    email:str=Field( unique=True, nullable=False)
    password: str

