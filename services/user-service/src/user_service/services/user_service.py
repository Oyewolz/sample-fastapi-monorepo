
from fastapi import HTTPException
from shared_lib.database.models.user.ft_user import FTUser
from shared_lib.dto.user import UserDto, UserLoginDto
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class UserService: 
    

    async def register_user(self, user: UserDto, session: AsyncSession): 
          
          if user.password != user.confirm_password: 
            raise ValueError("Passwords do not match")
          
          user_exist = await session.execute(select(FTUser).filter_by(email=user.email))
          if user_exist.scalars().first(): 
            raise HTTPException(status_code=400, detail="User already exists")

          ft_user = FTUser.model_validate(user)
          session.add(ft_user)
          await session.commit()
          await session.refresh(ft_user)

          del ft_user.password
          return ft_user
    
    async def login_user(self, user: UserLoginDto, session: AsyncSession):
        # find user by email
        result = await session.execute(select(FTUser).filter_by(email=user.email))
        userDto = result.scalars().first()
        if not userDto:
            raise HTTPException(status_code=400, detail="User not found")
        if userDto.password != user.password:
            raise HTTPException(status_code=400, detail="Invalid password")
        return userDto
 

    async def get_user(self, user_id: int, session: AsyncSession):
        user = await session.get(FTUser, user_id)
        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        return user

    async def update_user(self, user_id: int, userDto: UserDto, session: AsyncSession):
        user = await session.get(FTUser, user_id)
        if not user:
            raise HTTPException(status_code=400, detail="User not found")

        user.first_name = userDto.first_name
        user.last_name = userDto.last_name
        user.email = userDto.email
        user.password = userDto.password
        await session.commit()
        await session.refresh(user)
        return user
        

    async def delete_user(self, user_id: int, session: AsyncSession):
        user = await session.get(FTUser, user_id)
        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        await session.delete(user)
        await session.commit() 

