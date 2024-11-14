from pydantic import BaseModel, ConfigDict
from typing import Optional




class CreateProfileSchema(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    username: str
    
    model_config = ConfigDict(from_attributes=True)