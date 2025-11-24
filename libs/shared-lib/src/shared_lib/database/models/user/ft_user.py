
from ..base_entity import BaseEntity

class FTUser(BaseEntity, table=True):
    first_name: str
    last_name: str
    email: str
    password: str

