from datetime import datetime

from pydantic import Json

from ..base import CpObject


class FailNotification(CpObject):
    __name__ = "fail"

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
    reason: str
    reason_code: int
    operation_type: str
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
    data: Json = None
    token: str = None
    payment_method: str = None
    fall_back_scenario_declined_transaction_id: int = None
