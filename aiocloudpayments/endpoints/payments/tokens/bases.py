import abc

from ....typehints import NUMERIC
from ....types.transaction import Transaction
from ...base import CpEndpoint


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
