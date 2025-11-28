
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime
from sqlmodel import Field, SQLModel


class BaseEntity(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_type=DateTime(timezone=True),
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_type=DateTime(timezone=True),
    )
    deleted: Optional[bool] = Field(default=False, nullable=False)
    active: Optional[bool] = Field(default=True, nullable=False)
    
