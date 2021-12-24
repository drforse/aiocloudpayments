from datetime import datetime

from pydantic import Json

from ..base import CpObject


class ConfirmNotification(CpObject):
    __name__ = "confirm"

    transaction_id: int
    amount: float
    currency: str
    payment_amount: str
    payment_currency: str
    date_time: datetime
    card_first_six: str
    card_last_four: str
    card_type: str
    card_exp_date: str
    test_mode: bool
    status: str
    invoice_id: str = None
    account_id: str = None
    subscription_id: str = None
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
    auth_code: str = None
    data: Json = None
    token: str = None
    payment_method: str = None
