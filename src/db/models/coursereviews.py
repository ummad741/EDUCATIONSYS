from sqlalchemy import ForeignKey, Column, CheckConstraint, Integer
from sqlalchemy.orm import Mapped, mapped_column
# local files
from db.connection import BaseModel
from db.fields import created_at, str_20, full_text


class CourseReviewTable(BaseModel):

    # student courseni baholidi
    student_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
    comment: Mapped[full_text]
    created_at: Mapped[created_at]
    rating: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('rating BETWEEN 1 AND 5', name='check_rating_range')
    )
