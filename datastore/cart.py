import logging
from typing import Any, Tuple
from common_model.error import ErrorCode, ErrorResponse
from datastore.sql_datastore import SqlDataStore
from fastapi.encoders import jsonable_encoder


class CartDataStore:
    def __init__(self, datastore: SqlDataStore) -> None:
        self.datastore = datastore
        return

    # ----------------- Basic CRUD operations ----------------- #
    def get(self, id: int) -> Tuple[ProductDomainModel, ErrorResponse]:
        try:
            product = self.datastore.session.query(ProductDomainModel).filter(
                ProductDomainModel.id == id).first()
            if product == None:
                return None, ErrorResponse(
                    error_code=ErrorCode.NO_RECORDS_FOUND,
                    message=f'no product found with id - {id}'
                )

            return product, None
        except Exception as e:
            logging.warning(f'ProductDataStore::get - {e}')
            return None, ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )
        
    def create(self, product: ProductDomainModel) -> Tuple[ProductDomainModel, ErrorResponse]:
        try:
            self.datastore.session.add(product)
            self.datastore.session.commit()
            self.datastore.session.refresh(product)
            return product, None
        except Exception as e:
            logging.warning(f'ProductDataStore::create - {e}')
            return None, ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )

    def update(self, product: ProductDomainModel, updates: dict[str, Any]) -> Tuple[ProductDomainModel, ErrorResponse]:
        try:
            product_data = jsonable_encoder(product)
            for field in product_data:
                if field in updates:
                    setattr(product, field, updates[field])
            self.datastore.session.add(product)
            self.datastore.session.commit()
            self.datastore.session.refresh(product)
            return product, None
        except Exception as e:
            logging.warning(f'ProductDataStore::update - {e}')
            return None, ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )

    def delete(self, id: int) -> ErrorResponse:
        try:
            product = self.datastore.session.query(ProductDomainModel).filter(
                ProductDomainModel.id == id).first()

            if product == None:
                return ErrorResponse(
                    error_code=ErrorCode.NO_RECORDS_FOUND,
                    message=f'no user found with id - {id}'
                )
            self.datastore.session.delete(product)
            self.datastore.session.commit()
            return None
        except Exception as e:
            logging.warning(f'ProductDataStore::delete - {e}')
            return ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )

    # ----------------- Custom Query Operations ----------------- #
    def get_all_custom_query(self, query: str, params: dict) -> Tuple[Any, ErrorResponse]:
        try:
            products = self.datastore.session.execute(query, params)
            if products == None or len(products) == 0:
                return None, ErrorResponse(
                    error_code=ErrorCode.NO_RECORDS_FOUND,
                    message=f'no product found - {id}'
                )

            return products, None
        except Exception as e:
            logging.warning(f'ProductDataStore::get_all_custom_query - {e}')
            return None, ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )
