from sqlalchemy import Column, Float, ForeignKey, String, Boolean, text, Text
from sqlalchemy.orm import Mapped, mapped_column
# localfiles
from db.connection import BaseModel
from db.fields import str_20, str_50, full_text, created_at


class SubmissionsTable(BaseModel):

    __tablename__ = "submissions"

    submitted_at: Mapped[created_at]
    grade: Mapped[Float]
    # har bir topshiriqa talaba javob yuboradi
    student_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    assignment_id: Mapped[int] = mapped_column(ForeignKey('assignments.id'))
    feedback: Mapped[full_text]
