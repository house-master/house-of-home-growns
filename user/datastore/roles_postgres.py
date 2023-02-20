

# from typing import Any, Tuple
# from common_schema.error import ErrorCode, ErrorResponse
# from common_schema.user import UserRoleType
# from datastore.sql_datastore import SqlDataStore
# from user.domain.user import UserRoleDomainModel
# from fastapi.encoders import jsonable_encoder
# import logging


# class :
#     def __init__(self, datastore: SqlDataStore) -> None:
#         self.datastore = datastore
#         return

#     def get(self, email: str) -> Tuple[list[UserRoleDomainModel], ErrorResponse]:
#         try:
#             roles = self.datastore.session.query(UserRoleDomainModel).filter(
#                 UserRoleDomainModel.email == email).all()
#             if roles == None or len(roles) == 0:
#                 return None, ErrorResponse(
#                     error_code=ErrorCode.NO_RECORDS_FOUND,
#                     message=f'no user found with email - {email}'
#                 )

#             return roles, None
#         except Exception as e:
#             logging.warning(f'::get - {e}')
#             return None, ErrorResponse(
#                 error_code=ErrorCode.INTERNAL_SERVER_ERROR,
#                 message=f'{e}'
#             )

#     def create(self, role: UserRoleDomainModel) -> Tuple[UserRoleDomainModel, ErrorResponse]:
#         try:
#             self.datastore.session.add(role)
#             self.datastore.session.commit()
#             self.datastore.session.refresh(role)
#             return role, None
#         except Exception as e:
#             logging.warning(f'::create - {e}')
#             return None, ErrorResponse(
#                 error_code=ErrorCode.INTERNAL_SERVER_ERROR,
#                 message=f'{e}'
#             )

#     def createMultiple(self, roles: list[UserRoleDomainModel]) -> Tuple[UserRoleDomainModel, ErrorResponse]:
#         try:
#             for role in roles:
#                 self.datastore.session.add(role)
#                 self.datastore.session.commit()
#                 self.datastore.session.refresh(role)
#             return role, None
#         except Exception as e:
#             logging.warning(f'::create - {e}')
#             return None, ErrorResponse(
#                 error_code=ErrorCode.INTERNAL_SERVER_ERROR,
#                 message=f'{e}'
#             )

#     def update(self, role: UserRoleDomainModel, updates: dict[str, Any]) -> Tuple[UserRoleDomainModel, ErrorResponse]:
#         try:
#             user_data = jsonable_encoder(role)
#             for field in user_data:
#                 if field in updates:
#                     setattr(role, field, updates[field])
#             self.datastore.session.add(role)
#             self.datastore.session.commit()
#             self.datastore.session.refresh(role)
#             return role, None
#         except Exception as e:
#             logging.warning(f'::update - {e}')
#             return None, ErrorResponse(
#                 error_code=ErrorCode.INTERNAL_SERVER_ERROR,
#                 message=f'{e}'
#             )

        
#     def delete(self, email: str, role: UserRoleType) -> ErrorResponse:
#         try:
#             role = self.datastore.session.query(UserRoleDomainModel).filter(
#                 UserRoleDomainModel.email == email and UserRoleDomainModel.role == role.value).first()

#             if role == None:
#                 return ErrorResponse(
#                     error_code=ErrorCode.NO_RECORDS_FOUND,
#                     message=f'no user found with email - {email}'
#                 )
#             self.datastore.session.delete(role)
#             self.datastore.session.commit()
#             return None
#         except Exception as e:
#             logging.warning(f'::delete - {e}')
#             return ErrorResponse(
#                 error_code=ErrorCode.INTERNAL_SERVER_ERROR,
#                 message=f'{e}'
#             )
