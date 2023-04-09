from datetime import datetime
from common_model.baseModel import PydanticBaseModel


class CouponDiscountType(PydanticBaseModel):
    ABSOLUTE = "ABSOLUTE"
    PERCENT = "PERCENT"


class CouponDomainModel(PydanticBaseModel):
    id: int
    code: str
    issuer: str

    currency: str

    min_order_value: float

    discount_type: CouponDiscountType
    discount_value: float

    max_amount: float

    is_active: bool

    # metadata
    created_date: datetime
    updated_date: datetime
