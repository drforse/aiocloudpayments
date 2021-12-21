import abc
from typing import Optional

from .router import Router
from .. import AioCpClient


class BaseDispatcher(Router, abc.ABC):
    @property
    @abc.abstractmethod
    def ip_whitelist(self) -> Optional[set]:
        raise NotImplementedError

    @ip_whitelist.setter
    @abc.abstractmethod
    def ip_whitelist(self, value: Optional[set]):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def check_hmac(self) -> bool:
        raise NotImplementedError

    @check_hmac.setter
    @abc.abstractmethod
    def check_hmac(self, value: bool):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def cp_client(self) -> Optional[AioCpClient]:
        raise NotImplementedError

    @cp_client.setter
    @abc.abstractmethod
    def cp_client(self, value: Optional[AioCpClient]):
        raise NotImplementedError

    @abc.abstractmethod
    def run_app(
            self,
            cp_client: AioCpClient,
            path: str,
            pay_path: str = None,
            cancel_path: str = None,
            check_path: str = None,
            confirm_path: str = None,
            fail_path: str = None,
            recurrent_path: str = None,
            refund_path: str = None,
            allow_ips: set[str] = None,
            check_hmac: bool = True,
            **kwargs
    ):
        raise NotImplementedError
