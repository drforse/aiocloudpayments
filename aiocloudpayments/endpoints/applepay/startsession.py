from ..base import CpEndpoint, Request
from ...types.applepay_session import ApplepaySession


class CpApplepayStartsessionEndpoint(CpEndpoint):
    __returning__ = ApplepaySession

    validation_url: str
    payment_url: str = None

    def build_request(self) -> Request:
        return Request(
            endpoint=f"applepay/startsession",
            x_request_id=self.x_request_id
        )
