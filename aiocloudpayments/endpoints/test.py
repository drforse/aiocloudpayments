from .base import CpEndpoint, Request


class CpTestEndpoint(CpEndpoint):
    __returning__ = None

    def build_request(self) -> Request:
        return Request(endpoint="test", x_request_id=self.x_request_id)
