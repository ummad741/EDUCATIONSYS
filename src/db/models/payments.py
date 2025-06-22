from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, text, Integer
import enum
# local files
from db.connection import BaseModel
from db.fields import str_50, str_20, full_text, created_at, bank_amount_balance_12_2


class PaymentsTable(BaseModel):

    class Status(enum.Enum):
        pending = "Pending"
        paid = "Paid"
        failed = "Failed"

    # pullik kusrlaga yoziladigan payment
    student_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
    amount: Mapped[bank_amount_balance_12_2]
    paid_at: Mapped[created_at]
    status: Mapped[Status]
