from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import Optional, List, ForwardRef, TYPE_CHECKING
from src.apps.models import Community


class ReadProfileSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str
    
    model_config = ConfigDict(
            from_attributes=True,
            extra="forbid"
        )


class CreateProfileSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str
    
    model_config = ConfigDict(
            from_attributes=True,
            extra="forbid"
    )