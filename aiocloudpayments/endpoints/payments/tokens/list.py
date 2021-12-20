from typing import List

from ....types.token import Token
from ...base import CpEndpoint, Request


class CpTokensListEndpoint(CpEndpoint):
    __returning__ = List[Token]

    def build_request(self) -> Request:
        return Request(
            endpoint="payments/cards/topup",
            x_request_id=self.x_request_id
        )
