from common_domain.sql_model import SqlDatabaseBase
from sqlalchemy import Boolean, Column, Integer, Numeric, String, ARRAY, LargeBinary, DateTime


class ShippingOrderDomainModel(SqlDatabaseBase):
    __tablename__ = "product_shipping"

    id: Column(Integer, primary_key=True, index=True)
    order_ids: Column(ARRAY(Integer), nullable=False, index=True)

    delivery_partner: Column(String, nullable=False, index=True)
    is_cod: Column(Boolean, nullable=False, index=True)

    shipping_cost: Column(Numeric, nullable=False, index=True)

    source_address_id: Column(Integer, nullable=False, index=True)
    destination_address_id: Column(Integer, nullable=False, index=True)

    estimated_delivery_time: Column(String, nullable=False, index=True)
    status: Column(String, nullable=False, index=True)

    # metadata
    created_date: Column(DateTime, nullable=False)
    updated_date: Column(DateTime, nullable=False)
