from models import User
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from jose import jwt
from security import get_password_hash, verify_password, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
from typing import Optional
class CRUD:
    async def get_all_users(self, async_session:async_sessionmaker[AsyncSession]):
        """_summary_

        Args:
            async_session (async_sessionmaker[AsyncSession]): _description_

        Returns:
            _type_: _description_
        """
        async with async_session() as session:
            statement = select(User).order_by(User.username)

            result = await session.execute(statement)
            
            return result.scalars()
    
    async def add_user(self, async_session:async_sessionmaker[AsyncSession], user:User):
        """_summary_

        Args:
            async_session (async_sessionmaker[AsyncSession]): _description_
            user (User): _description_
        """
        async with async_session() as session:
            session.add(user)
            
            await session.commit()
            return user
    
    async def get_user_by_username(self, async_session:async_sessionmaker[AsyncSession], username:str):
        """_summary_

        Args:
            async_session (async_sessionmaker[AsyncSession]): _description_
            username (str): _description_

        Returns:
            _type_: _description_
        """
        async with async_session() as session:
            statement = select(User).filter(User.username == username)
            
            result = await session.execute(statement)
            
            return result.scalars().one()
    
    async def authenticate_user(self, async_session:async_sessionmaker[AsyncSession], username:str, password:str):
        """_summary_

        Args:
            async_session (async_sessionmaker[AsyncSession]): _description_
            username (str): _description_

        Returns:
            _type_: _description_
        """
        async with async_session() as session:
            statement = select(User).filter(User.username == username)
            
            result = await session.execute(statement)
            user = result.scalars().one()
            if not user:
                return False
            if not verify_password(password, user.hashed_password):
                return False
            return user
    
    async def create_access_token(self, data:dict, expires_delta:Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
        
    
    async def update_user(self, async_session:async_sessionmaker[AsyncSession], username:str, data):
        """_summary_

        Args:
            async_session (async_sessionmaker[AsyncSession]): _description_
            username (str): _description_
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        async with async_session() as session:
            user = await self.get_user_by_username(session, username)
            
            user.email = data['email']
            user.hashed_password = get_password_hash(data['password'])
            
            await session.commit()
            
            return user
    
    async def delete_user(self, async_session:async_sessionmaker[AsyncSession], user:User):
        """_summary_

        Args:
            async_session (async_sessionmaker[AsyncSession]): _description_
            user (User): _description_
        """
        async with async_session() as session:
            await session.delete(user)
            
            await session.commit()