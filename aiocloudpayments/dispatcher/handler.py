import dataclasses
import inspect

from .typehints import CALLBACK_TYPE, FUNC_FILTER, NOTIFICATION


@dataclasses.dataclass
class Handler:
    callback: CALLBACK_TYPE
    func_filter: FUNC_FILTER = None

    async def check_filter(self, notification: NOTIFICATION) -> bool:
        if self.func_filter is None:
            return True

        result = self.func_filter(notification)
        result = await result if inspect.iscoroutinefunction(self.func_filter) else result
        return bool(result)
