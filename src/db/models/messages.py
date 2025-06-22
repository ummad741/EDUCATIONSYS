from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, ForeignKey, text
# local files
from db.connection import BaseModel
from db.fields import str_20, str_50, full_text, created_at


class MessagesTable(BaseModel):

    # teacher va student ortasidagi chat un

    sender_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    receiver_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    message: Mapped[full_text]
    sent_at: Mapped[created_at]
