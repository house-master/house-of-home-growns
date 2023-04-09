

from datetime import datetime
from common_model.baseModel import PydanticBaseModel


class ShippingStatus(PydanticBaseModel):
    SHIPPED = "SHIPPED"
    NOT_SHIPPED = "NOT_SHIPPED"


class ShippingType(PydanticBaseModel):
    REGULAR = "REGULAR"
    RETURN = "RETURN"

class ShippingOrderDomainModel(PydanticBaseModel):
    id: int
    order_item_ids: int

    delivery_partner: str
    shipping_type: ShippingType
    is_cod: bool

    shipping_cost: float

    source_address_id: int # address id
    destination_address_id: int  # address id

    status: ShippingStatus

    # metadata
    created_date: datetime
    updated_date: datetime
