from typing import Any, Union, Callable, Awaitable, Optional

from .callback import Result
from ..types import RefundNotification, RecurrentNotification, PayNotification, FailNotification, \
    ConfirmNotification, CheckNotification, CancelNotification

NOTIFICATION = Union[RefundNotification, RecurrentNotification, PayNotification, FailNotification,
                     ConfirmNotification, CheckNotification, CancelNotification]

FUNC_FILTER = Union[Callable[[NOTIFICATION], Any], Callable[[NOTIFICATION], Awaitable[Any]]]
CALLBACK_TYPE = Callable[[NOTIFICATION], Awaitable[Optional[Result]]]
