from datetime import datetime
from typing import Any

from .base import CpObject
from ..pydantic_custom_fields import CpUnixDate
from ..typehints import NUMERIC


class Subscription(CpObject):
    id: str
    account_id: str
    description: str = None
    email: str = None
    amount: NUMERIC = None
    currency_code: int = None
    currency: str = None
    require_confirmation: bool = None
    start_date: CpUnixDate = None
    start_date_iso: datetime = None
    interval_code: int = None
    interval: str = None
    period: int = None
    max_periods: Any = None
    culture_name: str = None
    status_code: int = None
    status: str = None
    successful_transactions_number: int = None
    failed_transactions_number: int = None
    last_transaction_date: CpUnixDate = None
    last_transaction_date_iso: Any = None
    next_transaction_date: CpUnixDate = None
    next_transaction_date_iso: datetime = None
    receipt: Any = None
    failover_scheme_id: Any = None
