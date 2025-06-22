import enum
from sqlalchemy import Column, DateTime, Date, BOOLEAN, String, text
from sqlalchemy.orm import Mapped, mapped_column
# local files
from db.connection import BaseModel
from db.fields import str_20, str_50


class UsersTable(BaseModel):
    class Role(enum.Enum):
        student = "Student"
        instructor = "Instructor"
        admin = "Admin"

    __tablename__ = "users"

    username: Mapped[str_20] = mapped_column(unique=True)
    email: Mapped[str_50] = mapped_column(unique=True)
    password: Mapped[str_20]
    role: Mapped[Role]
