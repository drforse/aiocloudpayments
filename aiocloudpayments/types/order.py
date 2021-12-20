from datetime import datetime

from .base import CpObject
from ..pydantic_custom_fields import CpUnixDate
from ..typehints import NUMERIC


class Order(CpObject):
    id: str
    number: int = None
    amount: NUMERIC = None
    currency: str = None
    currency_code: int = None
    email: str = None
    phone: str = None
    description: str = None
    require_confirmation: bool = None
    url: str = None
    culture_name: str = None
    created_date: CpUnixDate = None
    created_date_iso: datetime = None
    payment_date: CpUnixDate = None
    payment_date_iso: datetime = None
    status_code: int = None
    status: str = None
    internal_id: int = None
