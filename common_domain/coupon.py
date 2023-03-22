from sqlalchemy import Boolean, Column, Integer, Numeric, String, ARRAY, LargeBinary, DateTime
from common_domain.sql_model import SqlDatabaseBase


class CouponDomainModel(SqlDatabaseBase):
    __tablename__ = "coupons"

    id: Column(Integer, primary_key=True, index=True)
    code: Column(String, nullable=False)
    issuer: Column(String, nullable=False)

    currency: Column(String, nullable=False)  # money or percent

    min_order_value: Column(Numeric, nullable=False)

    discount_type: Column(String, nullable=False)  # money or percent
    discount_value: Column(Numeric, nullable=False)

    max_amount: Column(Numeric, nullable=False) # max money to return

    is_active: Column(Boolean, nullable=False)  # max money to return

    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)
