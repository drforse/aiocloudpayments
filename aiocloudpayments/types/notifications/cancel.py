from datetime import datetime

from ..base import CpObject


class CancelNotification(CpObject):
    __name__ = "cancel"

    transaction_id: int
    amount: float
    date_time: datetime
    invoice_id: str = None
    account_id: str = None
    email: str = None
    data: dict = None
