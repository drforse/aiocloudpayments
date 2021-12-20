from ..base import CpEndpoint, Request


class CpSubscriptionsCancelEndpoint(CpEndpoint):
    __returning__ = None

    id: str

    def build_request(self) -> Request:
        return Request(
            endpoint="subscriptions/cancel",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
