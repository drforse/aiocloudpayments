import abc
from typing import Optional, Dict, Any, Generic, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from pydantic.utils import to_camel

from aiocloudpayments.types.transaction import Transaction
from aiocloudpayments.types.secure_3d import Secure3D

CpType = TypeVar("CpType", bound=Any)


class Request(BaseModel):
    endpoint: str
    json_str: str = None
    x_request_id: str = None
    x_signature: str = None

    @property
    def headers(self) -> Optional[Dict[str, str]]:
        result = {}
        if self.x_request_id:
            result.update({"X-Request-ID": self.x_request_id})
        if self.x_signature:
            result.update({"X-Signature": self.x_signature})
        return result or None


class Response(GenericModel, Generic[CpType]):
    success: bool = Field(alias="Success")
    message: Optional[str] = Field(alias="Message")
    model: Optional[CpType] = Field(None, alias="Model")

    def is_error(self):
        if self.success is True or isinstance(self.model, Secure3D):
            return False
        return True

    def is_payment_error(self):
        return self.success is False and isinstance(self.model, Transaction)


class CpEndpoint(abc.ABC, BaseModel):
    x_request_id: str = None
    x_signature: str = None

    @property
    @abc.abstractmethod
    def __returning__(self) -> type:
        pass

    @abc.abstractmethod
    def build_request(self) -> Request:
        pass

    def build_response(self, data: Dict[str, Any]) -> Response[CpType]:
        return Response[self.__returning__](**data)

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
