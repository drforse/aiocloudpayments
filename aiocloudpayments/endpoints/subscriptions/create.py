from datetime import datetime

from ..base import CpEndpoint, Request
from ...typehints import NUMERIC
from ...types.subscription import Subscription


class CpSubscriptionsCreateEndpoint(CpEndpoint):
    __returning__ = Subscription

    token: str
    account_id: str
    description: str
    email: str
    amount: NUMERIC
    currency: str
    require_confirmation: bool
    start_date: datetime
    interval: str
    period: int
    max_periods: int = None
    customer_receipt: dict = None

    def build_request(self) -> Request:
        return Request(
            endpoint="subscriptions/create",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
