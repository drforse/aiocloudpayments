from datetime import datetime

from pydantic import Json

from ..base import CpObject


class RefundNotification(CpObject):
    __name__ = "refund"

    transaction_id: int
    payment_transaction_id: int
    amount: float
    date_time: datetime
    operation_type: str
    invoice_id: str = None
    account_id: str = None
    email: str = None
    data: Json = None
