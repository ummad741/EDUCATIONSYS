from sqlalchemy import Numeric, String, Text, create_engine
from sqlalchemy.orm import Session, sessionmaker, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# local files
from connections import config
from db.fields import (
    intpk, created_at, updated_at, str_50, str_20, full_text,
    price_cost_10_2, discount_tax_6_2,

)

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

SessionLocalAsync = async_sessionmaker(
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


class BaseModel(Base):
    __abstract__ = True
    type_anotation_map = {
        str_20: String(20),
        str_50: String(50),
        price_cost_10_2: Numeric(10, 2),
        discount_tax_6_2: Numeric(6, 2)

    }
    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
