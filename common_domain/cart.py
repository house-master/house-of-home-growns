from sqlalchemy import Boolean, Column, Integer, String, ARRAY, LargeBinary, DateTime
from common_domain.sql_model import SqlDatabaseBase

class CartDomainModel(SqlDatabaseBase):
    __tablename__ = "user_cart"

    id: Column(Integer, primary_key=True, index=True)
    user_id: Column(Integer, nullable=False, index=True)
    product_id: Column(ARRAY(Integer), nullable=False, index=True)
    quantity: Column(ARRAY(Integer), nullable=False)

    # metadata
    updated_date: Column(DateTime, nullable=False)
