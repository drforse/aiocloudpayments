from .base import CpObject


class Token(CpObject):
    token: str
    account_id: str
    card_mask: str
    expiration_date_month: int
    expiration_date_year: int
