from sqlalchemy import Column, String, Boolean, text, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
# localfiles
from db.connection import BaseModel
from db.fields import str_20, str_50, full_text


class CoursesTable(BaseModel):
    __tablename__ = "courses"

    title: Mapped[str_50]
    description: Mapped[full_text]
    # har bir kursni userstabledagi instructor yaratadi
    instructor_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
