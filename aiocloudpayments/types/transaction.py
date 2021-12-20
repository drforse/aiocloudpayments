from datetime import datetime
from typing import Any

from .base import CpObject
from ..pydantic_custom_fields import CpUnixDate
from ..typehints import NUMERIC


class Transaction(CpObject):
    reason_code: int
    public_id: str
    terminal_url: str 
    transaction_id: int = None
    amount: NUMERIC = None
    currency: str = None
    currency_code: int = None
    payment_amount: int = None
    payment_currency: str = None
    payment_currency_code: int = None
    invoice_id: str = None
    account_id: str = None
    email: str = None
    description: str = None
    json_data: Any = None
    created_date: CpUnixDate = None
    payout_date: Any = None
    payout_date_iso: Any = None
    payout_amount: Any = None
    created_date_iso: datetime = None
    auth_date: CpUnixDate = None
    auth_date_iso: datetime = None
    confirm_date: CpUnixDate = None
    confirm_date_iso: datetime = None
    auth_code: Any = None
    test_mode: bool = None
    rrn: Any = None
    original_transaction_id: Any = None
    fall_back_scenario_declined_transaction_id: Any = None
    ip_address: str = None
    ip_country: str = None
    ip_city: str = None
    ip_region: str = None
    ip_district: str = None
    ip_latitude: int = None
    ip_longitude: int = None
    card_first_six: str = None
    card_last_four: str = None
    card_exp_date: str = None
    card_type: str = None
    card_product: Any = None
    card_category: Any = None
    escrow_accumulation_id: Any = None
    issuer_bank_country: str = None
    issuer: str = None
    card_type_code: int = None
    status: str = None
    status_code: int = None
    culture_name: str = None
    reason: str = None
    card_holder_message: str = None
    type: int = None
    refunded: bool = None
    name: str = None
    token: str = None
    subscription_id: Any = None
    gateway_name: str = None
    apple_pay: bool = None
    android_pay: bool = None
    wallet_type: str = None
    total_fee: int = None

    def get_error_message(self) -> str:
        return f"{self.reason_code}: {self.reason}"
