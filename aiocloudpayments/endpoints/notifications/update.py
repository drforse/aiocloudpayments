from ..base import CpEndpoint, Request


class CpNotificationsUpdateEndpoint(CpEndpoint):
    __returning__ = None

    type: str
    is_enabled: bool = None
    address: str = None
    http_method: str = None
    encoding: str = None
    format: str = None

    def build_request(self) -> Request:
        return Request(
            endpoint=f"site/notifications/{self.type}/update",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True, exclude_none=True)
        )
