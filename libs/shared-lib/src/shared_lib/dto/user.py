
from pydantic import BaseModel


class UserDto(BaseModel): 
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str 

class UserLoginDto(BaseModel): 
    email: str
    password: str


class AuthResponse(BaseModel): 
    first_name: str
    last_name: str
    access_token: str