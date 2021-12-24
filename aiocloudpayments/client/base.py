import asyncio
from http import HTTPStatus
from typing import Union

from aiohttp import ClientSession, BasicAuth, ClientError

from ..endpoints.base import CpEndpoint, CpType
from ..exceptions import CpNetworkError, CpTooManyRequests, CpBadRequestError, CpPaymentError, CpAPIError
from ..utils import json

DEFAULT_TIMEOUT = 300.0


class BaseCpClient:
    def __init__(
            self,
            public_id: str,
            api_secret: str,
            session: ClientSession = None,
            base_url: str = "https://api.cloudpayments.ru/",
            requests_timeout: Union[float, int] = DEFAULT_TIMEOUT
    ):
        self._public_id = public_id
        self._api_secret = api_secret
        self._session = session
        self._base_url = base_url
        self._default_timeout = requests_timeout

    async def get_session(self) -> ClientSession:
        if self._session is None or self._session.closed:
            self._session = ClientSession()
        return self._session

    async def request(self, endpoint: CpEndpoint, timeout: int = None) -> CpType:
        auth = BasicAuth(self._public_id, self._api_secret)
        request = endpoint.build_request()
        headers = {"Content-Type": "application/json"}
        headers.update(request.headers or {})

        try:
            session = await self.get_session()
            async with session.post(
                self._base_url + request.endpoint,
                data=request.json_str,
                headers=headers,
                timeout=self._default_timeout if timeout is None else timeout,
                auth=auth,
            ) as resp:
                raw_result = await resp.text()

        except asyncio.TimeoutError:
            raise CpNetworkError(endpoint, "Request timeout error")
        except ClientError as e:
            raise CpNetworkError(endpoint, f"{type(e).__name__}: {e}")
        response = self.check_response(endpoint=endpoint, status_code=resp.status, content=raw_result)
        return response.model

    @staticmethod
    def check_response(endpoint: CpEndpoint, status_code: int, content: str):
        json_data = json.loads(content)
        response = endpoint.build_response(json_data)
        if HTTPStatus.OK <= status_code <= HTTPStatus.IM_USED and response.is_error() is False:
            return response

        if response.is_payment_error():
            raise CpPaymentError(endpoint, response.model, response.model.get_error_message())

        if status_code == HTTPStatus.TOO_MANY_REQUESTS:
            raise CpTooManyRequests(endpoint, response.message)
        if status_code == HTTPStatus.BAD_REQUEST:
            raise CpBadRequestError(endpoint, response.message)

        raise CpAPIError(endpoint, response.message)

    async def disconnect(self):
        await self._session.close()
