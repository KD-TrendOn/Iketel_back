from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class UserModel(BaseModel):
    id : str
    username : str
    email : str
    password : str
    disabled : bool
    date_created : datetime
    
    model_config = ConfigDict(
        from_attributes=True
    )

class UserCreateModel(BaseModel):
    username : str
    email : str
    password : str
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example":{
                "username":"Пися",
                "email":"Кака",
                "password":"Попа"
            }
        }
    )

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserSchema(BaseModel):
    username: str
    email: Optional[str] = None
    disabled: Optional[bool] = None
    date_created : Optional[datetime] = None
    model_config = ConfigDict(
        from_attributes=True,
    )

class UserInDB(UserSchema):
    hashed_password:str
