from ..base import CpEndpoint, Request
from ...typehints import NUMERIC


class CpPaymentsRefundEndpoint(CpEndpoint):
    __returning__ = None

    transaction_id: int
    amount: NUMERIC
    json_data: dict = None

    def build_request(self) -> Request:
        return Request(
            endpoint="payments/refund",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
