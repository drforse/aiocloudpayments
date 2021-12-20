from ..base import CpEndpoint, Request
from ...types.transaction import Transaction


class CpPaymentsFindEndpoint(CpEndpoint):
    __returning__ = Transaction

    invoice_id: int

    def build_request(self) -> Request:
        return Request(
            endpoint="payments/find",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
