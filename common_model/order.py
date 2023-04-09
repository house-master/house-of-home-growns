from datetime import datetime
from enum import Enum
from common_model.baseModel import PydanticBaseModel
from common_model.payment import PaymentMethodType, PaymentStatusType


class OrderApprovalStatus(str, Enum):
    CREATED = "CREATED"
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"


class OrderItemModel(PydanticBaseModel):
    id: int
    product_id: int
    quantity: int

    coupon_id: int

    sub_total: float
    shipping_cost: float
    total: float

    discount: float
    coupon_discount: float

    amount_to_pay: float


class OrderDomainModel(PydanticBaseModel):
    id: int
    order_id: int
    user_id: int

    billing_address: int # billing address id
    shipping_address: int  # shipping address id

    order_item_ids: list[OrderItemModel]

    payment_method: PaymentMethodType
    payment_status: PaymentStatusType
    payment_id: int

    approval_status: OrderApprovalStatus

    # metadata
    created_date: datetime
    updated_date: datetime