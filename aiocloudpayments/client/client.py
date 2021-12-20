from datetime import date as date_, datetime
from typing import List, Union

from .base import BaseCpClient
from ..endpoints import CpTestEndpoint
from ..endpoints.payments import CpPaymentsFindEndpoint, CpPaymentsFindV2Endpoint,\
    CpPaymentsConfirmEndpoint, CpPaymentsGetEndpoint, CpPaymentsListEndpoint,\
    CpPaymentsRefundEndpoint, CpPaymentsVoidEndpoint
from ..endpoints.payments.tokens import CpTokensAuthEndpoint, CpTokensChargeEndpoint,\
    CpTokensListEndpoint, CpTokenTopupEndpoint
from ..endpoints.payments.cards import CpCardsAuthEndpoint, CpCardsChargeEndpoint, \
    CpCardsPost3dsEndpoint, CpCardsTopupEndpoint
from ..endpoints.subscriptions import CpSubscriptionsCancelEndpoint, CpSubscriptionsCreateEndpoint, \
    CpSubscriptionsFindEndpoint, CpSubscriptionsGetEndpoint, CpSubscriptionsUpdateEndpoint
from ..endpoints.orders import CpOrdersCreateEndpoint, CpOrdersCancelEndpoint
from ..endpoints.notifications import CpNotificationsGetEndpoint, CpNotificationsUpdateEndpoint
from ..endpoints.applepay import CpApplepayStartsessionEndpoint
from ..types import ApplepaySession, Notification, Order, Person, Secure3D, Subscription, Token,\
    Transaction, TransactionInList
from ..typehints import NUMERIC

DEFAULT_PAYLOAD_EXCLUDE = ["self", "timeout"]


def _payload(data: dict, exclude: list = None) -> dict:
    exclude = exclude + DEFAULT_PAYLOAD_EXCLUDE if exclude else DEFAULT_PAYLOAD_EXCLUDE
    result = data.copy()
    for item in exclude:
        if item in result:
            del result[item]
    return result


class AioCpClient(BaseCpClient):
    async def test(
            self,
            timeout: int = None,
            x_request_id: str = None
    ):
        endpoint = CpTestEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def confirm_payment(
            self,
            transaction_id: int,
            amount: NUMERIC,
            json_data: dict = None,
            timeout: int = None,
            x_request_id: str = None
    ):
        endpoint = CpPaymentsConfirmEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def get_payment(
            self,
            transaction_id: int,
            timeout: int = None,
            x_request_id: str = None
    ) -> Transaction:
        endpoint = CpPaymentsGetEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def list_payments(
            self,
            date: date_,
            time_zone: str,
            timeout: int = None,
            x_request_id: str = None
    ) -> List[TransactionInList]:
        endpoint = CpPaymentsListEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def refund_payment(
            self,
            transaction_id: int,
            amount: NUMERIC,
            json_data: dict = None,
            timeout: int = None,
            x_request_id: str = None
    ):
        endpoint = CpPaymentsRefundEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def void_payment(
            self,
            transaction_id: int,
            timeout: int = None,
            x_request_id: str = None
    ):
        endpoint = CpPaymentsVoidEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def find_payment(
            self,
            invoice_id: int,
            use_new_method: bool = True,
            timeout: int = None,
            x_request_id: str = None
    ) -> Transaction:
        payload = _payload(locals(), exclude=["use_new_method"])
        if use_new_method:
            endpoint = CpPaymentsFindV2Endpoint(**payload)
        else:
            endpoint = CpPaymentsFindEndpoint(**payload)
        return await self.request(endpoint, timeout=timeout)

    async def auth_token(
            self,
            amount: NUMERIC,
            account_id: str,
            token: str,
            currency: str = None,
            invoice_id: str = None,
            description: str = None,
            ip_address: str = None,
            email: str = None,
            json_data: dict = None,
            timeout: int = None,
            x_request_id: str = None
    ) -> Transaction:
        endpoint = CpTokensAuthEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def charge_token(
            self,
            amount: NUMERIC,
            account_id: str,
            token: str,
            currency: str = None,
            invoice_id: str = None,
            description: str = None,
            ip_address: str = None,
            email: str = None,
            json_data: dict = None,
            timeout: int = None,
            x_request_id: str = None
    ) -> Transaction:
        endpoint = CpTokensChargeEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def list_tokens(
            self,
            timeout: int = None,
            x_request_id: str = None
    ) -> List[Token]:
        endpoint = CpTokensListEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def topup_token(
            self,
            token: str,
            amount: NUMERIC,
            account_id: str,
            currency: str,
            invoice_id: str = None,
            payer: Person = None,
            receiver: Person = None,
            timeout: int = None,
            x_request_id: str = None,
            x_signature: str = None
    ) -> Transaction:
        endpoint = CpTokenTopupEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def auth_card(
            self,
            amount: NUMERIC,
            ip_address: str,
            card_cryptogram_packet: str,
            currency: str = None,
            name: str = None,
            payment_url: str = None,
            invoice_id: str = None,
            description: str = None,
            culture_name: str = None,
            account_id: str = None,
            email: str = None,
            payer: Person = None,
            json_data: dict = None,
            timeout: int = None,
            x_request_id: str = None
    ) -> Union[Secure3D, Transaction]:
        endpoint = CpCardsAuthEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def charge_card(
            self,
            amount: NUMERIC,
            ip_address: str,
            card_cryptogram_packet: str,
            currency: str = None,
            name: str = None,
            payment_url: str = None,
            invoice_id: str = None,
            description: str = None,
            culture_name: str = None,
            account_id: str = None,
            email: str = None,
            payer: Person = None,
            json_data: dict = None,
            timeout: int = None,
            x_request_id: str = None
    ) -> Union[Secure3D, Transaction]:
        endpoint = CpCardsChargeEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def post3ds(
            self,
            transaction_id: int,
            pa_res: str,
            timeout: int = None,
            x_request_id: str = None
    ) -> Transaction:
        endpoint = CpCardsPost3dsEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def topup_card(
            self,
            card_cryptogram_packet: str,
            amount: NUMERIC,
            currency: str,
            name: str = None,
            account_id: str = None,
            email: 	str = None,
            json_data: dict = None,
            invoice_id: str = None,
            description: str = None,
            payer: Person = None,
            receiver: Person = None,
            timeout: int = None,
            x_request_id: str = None,
            x_signature: str = None
    ) -> Transaction:
        endpoint = CpCardsTopupEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def cancel_subscription(
            self,
            id: str = None,
            timeout: int = None,
            x_request_id: str = None
    ):
        endpoint = CpSubscriptionsCancelEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def create_subscription(
            self,
            token: str,
            account_id: str,
            description: str,
            email: str,
            amount: NUMERIC,
            currency: str,
            require_confirmation: bool,
            start_date: datetime,
            interval: str,
            period: int,
            max_periods: int = None,
            customer_receipt: dict = None,
            timeout: int = None,
            x_request_id: str = None
    ) -> Subscription:
        endpoint = CpSubscriptionsCreateEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def find_subscriptions(
            self,
            account_id: str,
            timeout: int = None,
            x_request_id: str = None
    ) -> List[Subscription]:
        endpoint = CpSubscriptionsFindEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def get_subscription(
            self,
            id: str,
            timeout: int = None,
            x_request_id: str = None
    ) -> Subscription:
        endpoint = CpSubscriptionsGetEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def update_subscription(
            self,
            id: str,
            description: str = None,
            amount: NUMERIC = None,
            currency: str = None,
            require_confirmation: bool = None,
            start_date: datetime = None,
            interval: str = None,
            period: int = None,
            max_periods: int = None,
            customer_receipt: dict = None,
            culture_name: str = None,
            timeout: int = None,
            x_request_id: str = None
    ) -> Subscription:
        endpoint = CpSubscriptionsUpdateEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def create_order(
            self,
            amount: NUMERIC,
            description: str,
            currency: str = None,
            email: str = None,
            require_confirmation: bool = None,
            send_email: bool = None,
            invoice_id: str = None,
            account_id: str = None,
            offer_uri: str = None,
            phone: str = None,
            send_sms: bool = None,
            send_viber: bool = None,
            culture_name: str = None,
            subscription_behavior: str = None,
            success_redirect_url: str = None,
            fail_redirect_url: str = None,
            json_data: dict = None,
            timeout: int = None,
            x_request_id: str = None
    ) -> Order:
        endpoint = CpOrdersCreateEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def cancel_order(
            self,
            id: str,
            timeout: int = None,
            x_request_id: str = None
    ):
        endpoint = CpOrdersCancelEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def get_notification(
            self,
            type: str,
            timeout: int = None,
            x_request_id: str = None
    ) -> Notification:
        endpoint = CpNotificationsGetEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def update_notification(
            self,
            type: str,
            is_enabled: bool = None,
            address: str = None,
            http_method: str = None,
            encoding: str = None,
            format: str = None,
            timeout: int = None,
            x_request_id: str = None
    ):
        endpoint = CpNotificationsUpdateEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)

    async def applepay_startsession(
            self,
            validation_url: str,
            payment_url: str = None,
            timeout: int = None,
            x_request_id: str = None
    ) -> ApplepaySession:
        endpoint = CpApplepayStartsessionEndpoint(**_payload(locals()))
        return await self.request(endpoint, timeout=timeout)
