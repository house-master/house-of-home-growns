from pydantic import BaseModel
from bson.objectid import ObjectId


class PydanticBaseModel(BaseModel):
    class Config:
        orm_mode = True
        smart_union = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
