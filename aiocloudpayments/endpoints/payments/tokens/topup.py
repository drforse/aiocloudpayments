from ....typehints import NUMERIC
from ....types.person import Person
from ....types.transaction import Transaction
from ...base import CpEndpoint, Request


class CpTokenTopupEndpoint(CpEndpoint):
    __returning__ = Transaction

    token: str
    amount: NUMERIC
    account_id: str
    currency: str
    invoice_id: str = None
    payer: Person = None
    receiver: Person = None

    def build_request(self) -> Request:
        return Request(
            endpoint="payments/cards/topup",
            x_request_id=self.x_request_id,
            x_signature=self.x_signature,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
