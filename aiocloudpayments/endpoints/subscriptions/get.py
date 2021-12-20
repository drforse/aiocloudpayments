from ..base import CpEndpoint, Request
from ...types.subscription import Subscription


class CpSubscriptionsGetEndpoint(CpEndpoint):
    __returning__ = Subscription

    id: str

    def build_request(self) -> Request:
        return Request(
            endpoint="subscriptions/get",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
