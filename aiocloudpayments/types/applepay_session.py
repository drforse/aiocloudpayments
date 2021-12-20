from datetime import datetime

from .base import CpObject


class ApplepaySession(CpObject):

    epoch_timestamp: datetime = None
    expires_at: datetime = None
    merchant_session_identifier: str = None
    nonce: str = None
    merchant_identifier: str = None
    domain_name: str = None
    display_name: str = None
    signature: str = None
