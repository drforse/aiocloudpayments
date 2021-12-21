from datetime import datetime

from ..base import CpObject


class RecurrentNotification(CpObject):
    __name__ = "recurrent"

    id: str
    account_id: str
    description: str
    email: str
    amount: float
    currency: str
    require_confirmation: bool
    start_date: datetime
    interval: str
    period: int
    status: str
    successful_transactions_number: int
    failed_transactions_number: int
    max_periods: int = None
    last_transaction_date: datetime = None
    next_transaction_date: datetime = None
