from typing import Optional

from aiocloudpayments.endpoints.base import CpEndpoint


class AioCloudPaymentsError(Exception):
    pass


class DetailedAioCloudPaymentsError(AioCloudPaymentsError):
    url: Optional[str] = None

    def __init__(self, message: Optional[str]) -> None:
        self.message = message

    def __str__(self) -> str:
        message = self.message
        if self.url:
            message += f"\n(background on this error at: {self.url})"
        return message


class CpAPIError(DetailedAioCloudPaymentsError):
    def __init__(
        self,
        endpoint: CpEndpoint,
        message: str,
    ) -> None:
        super().__init__(message=message)
        self.endpoint = endpoint


class CpNetworkError(CpAPIError):
    pass


class CpTooManyRequests(CpAPIError):
    url = "https://developers.cloudpayments.ru/#printsip-raboty"


class CpBadRequestError(CpAPIError):
    pass


class CpPaymentError(DetailedAioCloudPaymentsError):
    url = "https://developers.cloudpayments.ru/#kody-oshibok"

    def __init__(
        self,
        endpoint: CpEndpoint,
        model,  # typing cp type
        message: Optional[str],
    ) -> None:
        super().__init__(message=message)
        self.endpoint = endpoint
        self.model = model
