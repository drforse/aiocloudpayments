from ..base import CpEndpoint, Request


class CpPaymentsVoidEndpoint(CpEndpoint):
    __returning__ = None

    transaction_id: int

    def build_request(self) -> Request:
        return Request(
            endpoint="payments/void",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
