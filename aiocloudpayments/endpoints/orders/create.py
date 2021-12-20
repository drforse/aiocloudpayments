from ..base import CpEndpoint, Request
from ...typehints import NUMERIC
from ...types.order import Order


class CpOrdersCreateEndpoint(CpEndpoint):
    __returning__ = Order

    amount: NUMERIC
    currency: str = None
    description: str
    email: str = None
    require_confirmation: bool = None
    send_email: bool = None
    invoice_id: str = None
    account_id: str = None
    offer_uri: str = None
    phone: str = None
    send_sms: bool = None
    send_viber: bool = None
    culture_name: str = None
    subscription_behavior: str = None
    success_redirect_url: str = None
    fail_redirect_url: str = None
    json_data: dict = None

    def build_request(self) -> Request:
        return Request(
            endpoint="orders/create",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
