from datetime import datetime
from common_model.baseModel import PydanticBaseModel


class WishlistModel(PydanticBaseModel):
    id: int
    user_id: str
    products: list[int] # list of product ids

    # metadata
    updated_date: datetime
