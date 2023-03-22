

from typing import Any, Tuple
from common_model.error import ErrorCode, ErrorResponse
from datastore.sql_datastore import SqlDataStore
from common_domain.user import UserDomainModel
from fastapi.encoders import jsonable_encoder
import logging
import sqlalchemy

from user.model.setting import Settings



class UserPostgresDatastore:
    def __init__(self, datastore: SqlDataStore) -> None:
        self.datastore = datastore
        return

    def get(self, email: str) -> Tuple[UserDomainModel, ErrorResponse]:
        try:
            user = self.datastore.session.query(UserDomainModel).filter(
                UserDomainModel.email == email).first()
            if user == None:
                return None, ErrorResponse(
                    error_code=ErrorCode.NO_RECORDS_FOUND,
                    message=f'no user found with email - {email}'
                )

            return user, None
        except Exception as e:
            logging.warning(f'UserPostgresDatastore::get - {e}')
            return None, ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )

    def create(self, user: UserDomainModel) -> Tuple[UserDomainModel, ErrorResponse]:
        try:
            self.datastore.session.add(user)
            self.datastore.session.commit()
            self.datastore.session.refresh(user)
            return user, None
        except Exception as e:
            logging.warning(f'UserPostgresDatastore::create - {e}')
            return None, ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )

    def update(self, user: UserDomainModel, updates: dict[str, Any]) -> Tuple[UserDomainModel, ErrorResponse]:
        try:
            user_data = jsonable_encoder(user)
            for field in user_data:
                if field in updates:
                    setattr(user, field, updates[field])
            self.datastore.session.add(user)
            self.datastore.session.commit()
            self.datastore.session.refresh(user)
            return user, None
        except Exception as e:
            logging.warning(f'UserPostgresDatastore::update - {e}')
            return None, ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )

        

    def delete(self, email: str) -> ErrorResponse:
        try:
            user = self.datastore.session.query(UserDomainModel).filter(
                UserDomainModel.email == email).first()

            if user == None:
                return ErrorResponse(
                    error_code=ErrorCode.NO_RECORDS_FOUND,
                    message=f'no user found with email - {email}'
                )
            self.datastore.session.delete(user)
            self.datastore.session.commit()
            return None
        except Exception as e:
            logging.warning(f'UserPostgresDatastore::delete - {e}')
            return ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )

    def create_table(self, email: str) -> ErrorResponse:
        try:
            user = self.datastore.session.query(UserDomainModel).filter(
                UserDomainModel.email == email).first()

            if user == None:
                return ErrorResponse(
                    error_code=ErrorCode.NO_RECORDS_FOUND,
                    message=f'no user found with email - {email}'
                )
            self.datastore.session.delete(user)
            self.datastore.session.commit()
            return None
        except Exception as e:
            logging.warning(f'UserPostgresDatastore::delete - {e}')
            return ErrorResponse(
                error_code=ErrorCode.INTERNAL_SERVER_ERROR,
                message=f'{e}'
            )