
from common_model.baseModel import PydanticBaseModel


class PaymentMethodType(PydanticBaseModel):
    DEBIT_CARD = "DEBIT_CARD"  # format is cardnumber:expiry
    CREDIT_CARD = "CREDIT_CARD"  # format is cardnumber:expiry
    NET_BANKING = "NET_BANKING"  # format is bank:net_banking_id
    UPI = "UPI"  # format is upi id
    COD = "COD"  # no private details


class PaymentStatusType(PydanticBaseModel):
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
