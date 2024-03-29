from sqlalchemy import Boolean, Column, Integer, String, ARRAY, LargeBinary, DateTime
from common_domain.sql_model import SqlDatabaseBase


# wishlist is designed to hold one product data in a row so that analytics is easy
class WishlistDomainModel(SqlDatabaseBase):
    __tablename__ = "user_wishlist"

    id: Column(Integer, primary_key=True, index=True)
    user_id: Column(Integer, nullable=False, index=True)
    product_id: Column(Integer, nullable=False, index=True)

    # metadata
    updated_date: Column(DateTime, nullable=False)
