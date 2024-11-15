from pydantic import BaseModel, ConfigDict
from typing import Optional


class ReadProfileSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str
    
    model_config = ConfigDict(from_attributes=True)


class CreateProfileSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str
    
    model_config = ConfigDict(from_attributes=True)