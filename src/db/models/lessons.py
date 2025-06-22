from sqlalchemy import Column, ForeignKey, String, Boolean, text, Text
from sqlalchemy.orm import Mapped, mapped_column
# lacalfiles
from db.connection import BaseModel
from db.fields import str_20, str_50, full_text


class LessonsTable(BaseModel):
    __tablename__ = "lessons"

    title: Mapped[str_50]
    content: Mapped[full_text]
    order: Mapped[int]

    # har bir kursda birn nechta dars boladi
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
