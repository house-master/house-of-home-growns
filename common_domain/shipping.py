from common_domain.sql_model import SqlDatabaseBase
from sqlalchemy import Boolean, Column, Integer, Numeric, String, ARRAY, LargeBinary, DateTime


class ShippingOrderDomainModel(SqlDatabaseBase):
    __tablename__ = "product_shipping"

    id: Column(Integer, primary_key=True, index=True)
    order_item_ids: Column(ARRAY(Integer), nullable=False)

    delivery_partner: Column(String, nullable=False)
    shipping_type: Column(String, nullable=False)
    is_cod: Column(Boolean, nullable=False)

    shipping_cost: Column(Numeric, nullable=False)

    source_address_id: Column(Integer, nullable=False)
    destination_address_id: Column(Integer, nullable=False)
    
    status: Column(String, nullable=False, index=True)

    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)
