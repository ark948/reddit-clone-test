from pydantic import BaseModel, ConfigDict



class CreateCommunitySchema(BaseModel):
    title: str
    about: str

    model_config = ConfigDict(from_attributes=True)