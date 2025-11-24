
from ..base_entity import BaseEntity

class Role(BaseEntity, table=True):
    name: str
    description: str
