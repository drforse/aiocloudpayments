import abc
import enum

from ....typehints import NUMERIC
from ....types.transaction import Transaction
from ...base import CpEndpoint


class TrInitiatorCode(enum.IntEnum):
    SERVICE_INITIATED = 0
    CLIENT_INITIATED = 1


class PaymentScheduled(enum.IntEnum):
    ONCE = 0
    SCHEDULED = 1


class CpTokensChargeAuthEndpoint(CpEndpoint, abc.ABC):
    __returning__ = Transaction

    amount: NUMERIC
    currency: str = None
    account_id: str
    token: str
    invoice_id: str = None
    description: str = None
    ip_address: str = None
    email: str = None
    json_data: dict = None
    tr_initiator_code: int
    payment_scheduled: int = None  # Note: required if tr_initiator_code is SERVICE_INITIATED
