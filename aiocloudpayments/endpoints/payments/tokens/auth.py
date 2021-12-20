from .bases import CpTokensChargeAuthEndpoint
from ...base import Request


class CpTokensAuthEndpoint(CpTokensChargeAuthEndpoint):

    def build_request(self) -> Request:
        return Request(
            endpoint="payments/tokens/auth",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
