from __future__ import annotations
from typing import Tuple
from sqlalchemy import Boolean, Column, Integer, String, ARRAY, LargeBinary, DateTime
from sqlalchemy.orm import relationship

from common_domain.sql_model import SqlDatabaseBase


class UserDomainModel(SqlDatabaseBase):
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



class UserAddressDomainModel(SqlDatabaseBase):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)

    name = Column(String, nullable=False)

    contact_person_name = Column(String, nullable=False)
    mobile_number = Column(String, nullable=False)

    line_1 = Column(String, nullable=False)
    line_2 = Column(String, nullable=False)
    landmark = Column(String)

    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    pin_code = Column(String, nullable=False)

    address_type = Column(String, nullable=False)

    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)


class UserBehaviorDomainModel(SqlDatabaseBase):
    __tablename__ = "user_behavior"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)

    user_choice_type = Column(String, nullable=False)
    user_buyer_type = Column(String, nullable=False)

    last_purchase_date = Column(DateTime)
    
    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)


