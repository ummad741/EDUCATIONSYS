from sqlalchemy import Column, ForeignKey, Boolean, text
from sqlalchemy.orm import Mapped, mapped_column
# local files
from db.connection import BaseModel
from db.fields import str_50, str_20, full_text, created_at


class EnrolmentsTable(BaseModel):

    # talabaning kursga yozliganligini belgilaydi
    student_id: Mapped[int] = mapped_column(
        ForeignKey('users.id')
    )
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
    enrolled_at: Mapped[created_at]
