from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, Boolean, text, Text
from sqlalchemy.orm import Mapped, mapped_column
# local files
from db.connection import BaseModel
from db.fields import str_20, str_50, full_text


class AssignmentsTable(BaseModel):
    __tablename__ = "assignments"

    title: Mapped[str_50]
    description: Mapped[full_text]
    due_data: Mapped[datetime]

    # har bir kursga topshiriq beriladi
    lesson_id: Mapped[int] = mapped_column(ForeignKey('lessons.id'))
