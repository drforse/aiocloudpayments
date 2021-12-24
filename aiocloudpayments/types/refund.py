from datetime import datetime, date

from .base import CpObject


class Refund(CpObject):
    transaction_id: int
