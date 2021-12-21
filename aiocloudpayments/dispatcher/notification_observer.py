from typing import List, Callable

from .callback import Result
from .handler import Handler
from .typehints import CALLBACK_TYPE, FUNC_FILTER, NOTIFICATION


class NotificationObserver:
    def __init__(self):
        self.handlers: List[Handler] = []

    def register(self, callback: CALLBACK_TYPE, func_filter: FUNC_FILTER = None) -> Handler:
        handler = Handler(callback, func_filter)
        self.handlers.append(handler)
        return handler

    async def trigger(self, notification: NOTIFICATION) -> Result:
        for handler in self.handlers:
            result = await handler.check_filter(notification)
            if result is False:
                continue
            result = await handler.callback(notification)
            if result == Result.SKIP:
                continue
            return result if result is not None else Result.OK
        return Result.SKIP

    def __call__(self, func_filter: FUNC_FILTER = None) -> Callable[[CALLBACK_TYPE], CALLBACK_TYPE]:
        def wrapper(callback: CALLBACK_TYPE) -> CALLBACK_TYPE:
            self.register(callback, func_filter)
            return callback
        return wrapper
