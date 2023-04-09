from common_domain.sql_model import SqlDatabaseBase
from sqlalchemy import Boolean, Column, Integer, Numeric, String, ARRAY, LargeBinary, DateTime



class ProductReviewCommentDomainModel(SqlDatabaseBase):
    __tablename__ = "product_review_comments"

    id: Column(Integer, primary_key=True, index=True)
    product_id: Column(Integer, nullable=False, index=True)
    user_id: Column(Integer, nullable=False, index=True)
    rating: Column(Integer)
    title: Column(String, nullable=False)
    content: Column(String, nullable=False)
    images: Column(ARRAY(String))
    is_visible: Column(Boolean, nullable=False)

    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)
    

class ProductInventoryDomainModel(SqlDatabaseBase):
    __tablename__ = "product_inventory"

    id: Column(Integer, primary_key=True, index=True)
    product_id: Column(Integer, nullable=False, index=True)
    quantity: Column(Integer, nullable=False)  # user id
    city: Column(String)
    location: Column(String)

    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)


class ProductDomainModel(SqlDatabaseBase):
    __tablename__ = "products"

    id: Column(Integer, primary_key=True, index=True)

    vendor_id: Column(Integer, nullable=False, index=True)  # user id

    name: Column(String, nullable=False)
    alias: Column(String, nullable=False)

    category: Column(String, nullable=False, index=True)
    sub_category: Column(String, nullable=False, index=True)

    thumbnail: Column(String)
    
    description: Column(String, nullable=False)
    sub_description: Column(String, nullable=False)
    images: Column(ARRAY(String))
    
    currency: Column(String, nullable=False)
    price: Column(Numeric, nullable=False)
    discount: Column(Numeric, nullable=False)

    featured_state: Column(String, nullable=False)

    is_active: Column(Boolean, nullable=False)
    
    verification_state: Column(String, nullable=False)
    
    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)
