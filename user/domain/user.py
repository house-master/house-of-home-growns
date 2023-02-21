from __future__ import annotations
from typing import Tuple
from sqlalchemy import Boolean, Column, Integer, String, ARRAY, LargeBinary
from sqlalchemy.orm import relationship

from user.domain.sql_model import DatabaseBase


class UserDomainModel(DatabaseBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    mobile_number = Column(String, unique=True, index=True)
    hashed_password = Column(LargeBinary, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    icon = Column(String)
    roles = Column(ARRAY(String), nullable=False)
    account_status = Column(String, nullable=False)
    login_status = Column(String, nullable=False)



# class UserAddressDomainModel(DatabaseBase):
#     __tablename__ = "address"

#     email = Column(String, primary_key=True, index=True)    

#     name = Column(String, nullable=False)

#     contact_person_name = Column(String, nullable=False)
#     mobile_number = Column(String, nullable=False)

#     line_1 = Column(String, nullable=False)
#     line_2 = Column(String, nullable=False)

#     landmark = Column(String)

#     state = Column(String, nullable=False)
#     city = Column(String, nullable=False)

#     pin_code = Column(String, nullable=False)

#     address_type = Column(String, nullable=False)
#     timing_type = Column(String, nullable=False)
