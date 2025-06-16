from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src import config


engine = create_engine(
    url=config.DB_URL,
    echo=True,
    pool_size=5
)

async_engine = create_async_engine(
    url=config.ASYNC_DB_URL,
    echo=True,
    pool_size=5,
)

SessionLocal = sessionmaker(
    bind=async_engine,
    autoflush=False,
    autocommit=False
)
SyncSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()