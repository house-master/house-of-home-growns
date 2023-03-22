# from sqlalchemy import Boolean, Column, Integer, String, ARRAY, LargeBinary, DateTime
# from common_domain.sql_model import SqlDatabaseBase


# class ContentDomainModel(SqlDatabaseBase):
#     __tablename__ = "content"

#     content_type: Column(Integer, primary_key=True, index=True)
#     content_sub_type: Column(Integer, primary_key=True, index=True)

#     heading: Column(String, nullable=False)
#     user_id: Column(Integer, nullable=False, index=True)
#     product_id: Column(Integer, nullable=False, index=True)
#     quantity: Column(Integer, nullable=False)

#     # metadata
#     updated_date: Column(DateTime, nullable=False)
