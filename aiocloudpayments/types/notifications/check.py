from datetime import datetime

from ..base import CpObject


class CheckNotification(CpObject):
    __name__ = "check"

    transaction_id: int
    amount: float
    currency: str
    payment_amount: str
    payment_currency: str
    datetime: datetime
    card_first_six: str
    card_last_four: str
    card_type: str
    card_exp_date: str
    test_mode: bool
    status: str
    operation_type: str
    invoice_id: str = None
    account_id: str = None
    subscription_id: str = None
    token_recipient: str = None
    name: str = None
    email: str = None
    ip_address: str = None
    ip_country: str = None
    ip_city: str = None
    ip_region: str = None
    ip_district: str = None
    ip_latitude: str = None
    ip_longitude: str = None
    issuer: str = None
    issuer_bank_country: str = None
    description: str = None
    card_product: str = None
    payment_method: str = None
    data: dict = None
