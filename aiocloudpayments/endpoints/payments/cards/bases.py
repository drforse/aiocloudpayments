import abc
from typing import Union

from ....typehints import NUMERIC
from ....types.person import Person
from ....types.transaction import Transaction
from ....types.secure_3d import Secure3D
from ...base import CpEndpoint


class CpCardsChargeAuthEndpoint(CpEndpoint, abc.ABC):
    __returning__ = Union[Secure3D, Transaction]

    amount: NUMERIC
    currency: str = None
    ip_address: str
    card_cryptogram_packet: str
    name: str = None
    payment_url: str = None
    invoice_id: str = None
    description: str = None
    culture_name: str = None
    account_id: str = None
    email: str = None
    payer: Person = None
    json_data: dict = None
