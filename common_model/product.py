from datetime import datetime
from typing import Optional
from common_model.baseModel import PydanticBaseModel
from enum import Enum


class ProductVerificationStatus(str, Enum):
    VERIFICATION_PENDING = "VERIFICATION_PENDING"
    VERIFICATION_COMPLETE = "VERIFICATION_COMPLETE"


class ProductReviewCommentModel(PydanticBaseModel):
    id: Optional[str]
    product_id: int
    creator: str
    rating: int
    title: str
    content: str  # vendor type user email
    images: list[str]
    is_visible: bool

    # metadata
    updated_date: datetime
    updated_date: datetime


class ProductModel(PydanticBaseModel):
    id: Optional[str]
    name: str
    alias: str 
    category: str
    sub_category: str
    description: str
    owner: str # vendor type user email
    images: list[str]
    verification_state: ProductVerificationStatus
    
    # metadata
    updated_date: datetime
    updated_date: datetime
