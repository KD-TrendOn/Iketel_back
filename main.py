from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from crud import CRUD
from db import engine
from schemas import UserModel, UserCreateModel
from typing import List
from models import User
import uuid 
from http import HTTPStatus
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os



app = FastAPI(
    title="Iketel API",
    description="Backend of storymaker service",
    docs_url="/"
)





session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

db = CRUD()

@app.get('/users', response_model=List[UserModel])
async def all_users():
    notes = await db.get_all_users(session)
    
    return notes

@app.post('/register', status_code=HTTPStatus.CREATED)
async def create_user(user_data:UserCreateModel):
    new_user = User(
        id = str(uuid.uuid4()),
        username = user_data.username,
        email = user_data.email,
        password = user_data.email,
    )
    user = await db.add_user(session, new_user)