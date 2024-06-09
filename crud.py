from models import User
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

class CRUD:
    async def get_all_users(self, async_session:async_sessionmaker[AsyncSession]):
        """_summary_

        Args:
            async_session (async_sessionmaker[AsyncSession]): _description_

        Returns:
            _type_: _description_
        """
        async with async_session() as session:
            statement = select(User).order_by(User.id)

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
    
    async def get_user_by_id(self, async_session:async_sessionmaker[AsyncSession], user_id:str):
        async with async_session() as session:
            statement = select(User).filter(User.id == user_id)
            
            result = await session.execute(statement)
            
            return result.scalars().one()
    
    await def get_user_by_username(self, async_session:async_sessionmaker[AsyncSession], username:str)
    
    async def update_user(self, async_session:async_sessionmaker[AsyncSession], user_id:str, data):
        
        async with async_session() as session:
            user = await self.get_user_by_id(session, user_id)
            
            user.username = data['username']
            user.email = data['email']
            user.password = data['password']
            
            await session.commit()
            
            return user
    
    async def delete_user(self, async_session:async_sessionmaker[AsyncSession], user:User):
        async with async_session() as session:
            await session.delete(user)
            
            await session.commit()