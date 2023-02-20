from __future__ import annotations
from typing import Tuple
from sqlalchemy import Boolean, Column, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from user.domain.sql_model import DatabaseBase


class UserDomainModel(DatabaseBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    mobile_number = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    icon = Column(String)
    roles = Column(ARRAY(String), nullable=False)
    account_status = Column(String, nullable=False)
    


# class UserRoleDomainModel(DatabaseBase):
#     __tablename__ = "roles"

#     email = Column(String, primary_key=True, index=True)
#     role = Column(String)

#     @staticmethod
#     def GenerateDiff(old: list[UserRoleDomainModel], new: list[UserRoleDomainModel]) -> Tuple[list[str], list[str]]:
#         old_roles = [entry.role for entry in old]
#         new_roles = [entry.role for entry in new]

#         deleted_roles = list(set(old_roles) - set(new_roles))
#         created_roles = list(set(new_roles) - set(old_roles))

#         return created_roles, deleted_roles



class UserAddressDomainModel(DatabaseBase):
    __tablename__ = "address"

    email = Column(String, primary_key=True, index=True)    

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
    timing_type = Column(String, nullable=False)
