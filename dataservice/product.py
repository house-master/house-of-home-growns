from typing import Any, Tuple
from common_model.error import ErrorResponse
from common_model.product import ProductModel
from common_domain.product import ProductDomainModel
from datastore.product import ProductDataStore


class ProductDataService:
    def __init__(self, datastore: ProductDataStore) -> None:
        self.datastore = datastore
        return

    def get_all(self, skip: int  = 0, limit: int = 0) -> Tuple[list[ProductModel], ErrorResponse]:
        products, err = self.datastore.get_all(skip, limit)
        if err != None:
            return None, err

        output = []
        for product in products:
            output.append(ProductModel(**(product.__dict__)))

        return output, None

    def get_all_by_category(self, category: str, skip: int = 0, limit: int = 0) -> Tuple[list[ProductModel], ErrorResponse]:
        products, err = self.datastore.get_all_by_category(category, skip, limit)
        if err != None:
            return None, err

        output = []
        for product in products:
            output.append(ProductModel(**(product.__dict__)))

        return output, None

    def get_all_by_creator(self, creator_id: int, skip: int = 0, limit: int = 0) -> Tuple[list[ProductModel], ErrorResponse]:
        products, err = self.datastore.get_all_by_creator(
            creator_id, skip, limit)
        if err != None:
            return None, err

        output = []
        for product in products:
            output.append(ProductModel(**(product.__dict__)))

        return output, None

    def get(self, id: int) -> Tuple[ProductModel, ErrorResponse]:
        product, err = self.datastore.get(id)
        if err != None:
            return None, err

        output = ProductModel(**(product.__dict__))

        return output, None
        
    def create(self, product: ProductModel) -> Tuple[ProductModel, ErrorResponse]:
        productDomain = ProductDomainModel(**product.dict())

        createdProduct, err = self.datastore.create(productDomain)
        if err != None:
            return None, err

        output = ProductModel(**(createdProduct.__dict__))

        return output, None

    def update(self, product: ProductModel, updates: dict[str, Any]) -> Tuple[ProductModel, ErrorResponse]:
        productDomain = ProductDomainModel(**product.dict())

        updatedProduct, err = self.datastore.update(productDomain, updates)
        if err != None:
            return None, err

        output = ProductModel(**(updatedProduct.__dict__))

        return output, None

    def delete(self, id: int) -> ErrorResponse:
        return self.datastore.delete(id)
