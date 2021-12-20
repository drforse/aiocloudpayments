from ....types.transaction import Transaction
from ...base import CpEndpoint, Request


class CpCardsPost3dsEndpoint(CpEndpoint):
    __returning__ = Transaction

    transaction_id: int
    pa_res: str

    def build_request(self) -> Request:
        return Request(
            endpoint="payments/cards/post3ds",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
