

from datetime import datetime
from common_model.baseModel import PydanticBaseModel
from common_model.product import ProductQuantityModel



class CartModel(PydanticBaseModel):
    id: int
    user_id: str
    products: list[ProductQuantityModel]

    # metadata
    updated_date: datetime
