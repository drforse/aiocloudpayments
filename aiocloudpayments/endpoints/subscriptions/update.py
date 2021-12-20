from datetime import datetime

from ..base import CpEndpoint, Request
from ...typehints import NUMERIC
from ...types.subscription import Subscription


class CpSubscriptionsUpdateEndpoint(CpEndpoint):
    __returning__ = Subscription

    id: str
    description: str = None
    amount: NUMERIC = None
    currency: str = None
    require_confirmation: bool = None
    start_date: datetime = None
    interval: str = None
    period: int = None
    max_periods: int = None
    customer_receipt: dict = None
    culture_name: str = None

    def build_request(self) -> Request:
        return Request(
            endpoint="subscriptions/update",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
