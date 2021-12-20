from .base import CpObject


class Notification(CpObject):
    is_enabled: bool = None
    address: str = None
    http_method: str = None
    encoding: str = None
    format: str = None
