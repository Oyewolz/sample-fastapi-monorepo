
from datetime import datetime, UTC
from typing import Optional

from sqlmodel import Field, SQLModel


class BaseEntity(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(UTC), nullable=False
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(UTC), nullable=False
    )
    deleted: Optional[bool] = Field(default=False, nullable=False)
    active: Optional[bool] = Field(default=True, nullable=False)
    
