from datetime import datetime
from decimal import Decimal
from typing import Annotated
from sqlalchemy import Text, text
from sqlalchemy.orm import mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime,
    mapped_column(server_default=text('TIMEZONE(utc, now())'))
]


updated_at = Annotated[
    datetime,
    mapped_column(
        server_default=text('TIMEZONE(utc, now())'),
        onupdate=datetime.utcnow
    )
]

str_50 = Annotated[str, 50]
str_20 = Annotated[str, 20]

# Decimal precision reqam soni scale . keyingi son
price_cost_10_2 = Annotated[Decimal, 10]
bank_amount_balance_12_2 = Annotated[Decimal, 12]
forex_stocks_15_4 = Annotated[Decimal, 15]
discount_tax_6_2 = Annotated[Decimal, 6]

full_text = Annotated[str, mapped_column(Text, deferred=True)]
