from ..base import CpEndpoint, Request
from ...types.notification_info import NotificationInfo


class CpNotificationsGetEndpoint(CpEndpoint):
    __returning__ = NotificationInfo

    type: str

    def build_request(self) -> Request:
        return Request(
            endpoint=f"site/notifications/{self.type}/get",
            x_request_id=self.x_request_id
        )
