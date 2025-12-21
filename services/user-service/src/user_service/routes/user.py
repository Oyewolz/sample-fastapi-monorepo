from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from shared_lib.database import get_session
from shared_lib.dto.api_response import ApiResponse
from shared_lib.dto.user import AuthResponse, UserDto, UserLoginDto
from user_service.services.user_service import UserService


router = APIRouter()


user_service = UserService()

@router.post("/", response_model=ApiResponse[UserDto])
async def register_user(user: UserDto, session: AsyncSession = Depends(get_session)):
     await user_service.register_user(user, session)
     return ApiResponse(data=user, message="User registered successfully")

@router.post("/login", response_model=ApiResponse[AuthResponse]) 
async def login_user( user: UserLoginDto, session: AsyncSession = Depends(get_session)): 
    access_token = await user_service.login_user(user, session)
    return ApiResponse(data=access_token, message="User logged in successfully")

@router.get("/{user_id}", response_model=ApiResponse[UserDto]) 
async def get_user( user_id: int, session: AsyncSession = Depends(get_session)): 
    user = await user_service.get_user(user_id, session)
    return ApiResponse(data=user, message="User retrieved successfully")

@router.put("/{user_id}", response_model=ApiResponse[UserDto]) 
async def update_user( user_id: int, user: UserDto, session: AsyncSession = Depends(get_session)): 
    await user_service.update_user(user_id, user, session)
    return ApiResponse(data=user, message="User updated successfully")

@router.delete("/{user_id}", response_model=ApiResponse[UserDto]) 
async def delete_user( user_id: int, session: AsyncSession = Depends(get_session)): 
     await user_service.delete_user(user_id, session)
     return ApiResponse(data=None, message="User deleted successfully")
