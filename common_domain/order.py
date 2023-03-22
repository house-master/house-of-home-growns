from sqlalchemy import Boolean, Column, Integer, Numeric, String, ARRAY, LargeBinary, DateTime
from common_domain.sql_model import SqlDatabaseBase


# multiple rows per order, per row one product
class OrderDomainModel(SqlDatabaseBase):
    __tablename__ = "order"

    id: Column(Integer, primary_key=True, index=True)
    order_id: Column(Integer, nullable=False, index=True)
    user_id: Column(Integer, nullable=False, index=True)

    product_id: Column(Integer, nullable=False, index=True)
    quantity: Column(Integer, nullable=False, index=True)

    billing_address: Column(Integer, nullable=False, index=True)  # address_id
    shipping_address: Column(Integer, nullable=False, index=True)  # shipping_id

    order_value_id: Column(Integer, nullable=False)

    payment_method: Column(String, nullable=False)
    payment_id: Column(Integer)

    approval_status: Column(String, nullable=False)

    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)


# multiple rows per order, per row one product
class OrderValueDomainModel(SqlDatabaseBase):
    __tablename__ = "order_value"

    id: Column(Integer, primary_key=True, index=True)
    coupon_id: Column(Integer, index=True)

    sub_total: Column(Numeric, nullable=False)
    shipping_cost: Column(Numeric, nullable=False)
    total: Column(Numeric, nullable=False)

    discount: Column(Numeric)
    coupon_discount: Column(Numeric)

    amount_to_pay: Column(Numeric, nullable=False)
