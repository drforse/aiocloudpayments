import logging
from typing import Optional, List

from .callback import Result
from ..dispatcher.notification_observer import NotificationObserver
from .typehints import NOTIFICATION

logger = logging.getLogger("aiocloudpayments.dispatcher.router")


class Router:
    def __init__(self, index: int = None):
        self.index = index

        self._parent_router: Optional[Router] = None
        self.sub_routers: List[Router] = []

        self.check = NotificationObserver()
        self.pay = NotificationObserver()
        self.fail = NotificationObserver()
        self.confirm = NotificationObserver()
        self.refund = NotificationObserver()
        self.recurrent = NotificationObserver()
        self.cancel = NotificationObserver()

        self._observers = {
            "check": self.check,
            "pay": self.pay,
            "fail": self.fail,
            "confirm": self.confirm,
            "refund": self.refund,
            "recurrent": self.recurrent,
            "cancel": self.cancel
        }

    @property
    def parent_router(self):
        return self._parent_router

    def include_router(self, router: 'Router') -> 'Router':
        """
        Attach another router.
        :param router:
        :return:
        """
        if not isinstance(router, Router):
            raise ValueError(f"router should be instance of Router not {type(router).__name__!r}")
        if self._parent_router:
            raise RuntimeError(f"Router is already attached to {self._parent_router!r}")
        if self == router:
            raise RuntimeError("Self-referencing routers is not allowed")

        parent: Optional[Router] = router
        while parent is not None:
            if parent == self:
                raise RuntimeError("Circular referencing of Router is not allowed")
            parent = parent.parent_router

        router._parent_router = self
        self.sub_routers.append(router)

        return router

    async def process_notification(self, notification: NOTIFICATION) -> Result:
        observer = self._observers.get(notification.__name__)
        result = await observer.trigger(notification)
        if result != Result.SKIP:
            return result
        for router in self.sub_routers:
            result = await router.process_notification(notification)
            if result != Result.SKIP:
                return result
        logger.warning(f"Notification was sent to server, but not handled: {notification}")
        return Result.SKIP

    def __str__(self):
        return f"{type.__class__.__name__}({self.index})"

    def __repr__(self):
        return f"<{self}>"
