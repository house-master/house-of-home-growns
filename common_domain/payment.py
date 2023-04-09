from __future__ import annotations
from typing import Tuple
from sqlalchemy import Boolean, Column, Integer, String, ARRAY, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from common_domain.sql_model import SqlDatabaseBase

# private data is like in case of card the card details, or upi details or net banking etc
class UserPaymentDetailDomainModel(SqlDatabaseBase):
    __tablename__ = "payment_detail"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(int, index=True)

    method_type = Column(String, nullable=False)

    # for card the card number
    # for net banking bank and IFSE
    private_data = Column(String, nullable=False)  # this is encrypted