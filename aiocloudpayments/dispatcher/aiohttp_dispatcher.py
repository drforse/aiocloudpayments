import logging

from aiohttp import web
from aiohttp.abc import Application

from .callback import Result
from .router import Router
from ..types.notifications import CancelNotification, CheckNotification, ConfirmNotification, \
    FailNotification, PayNotification, RecurrentNotification, RefundNotification
from ..utils import json


logger = logging.getLogger("aiocloudpayments.dispatcher")

NOTIFICATION_TYPES = {
    "pay": PayNotification, "cancel": CancelNotification, "check": CheckNotification,
    "confirm": ConfirmNotification, "fail": FailNotification,
    "recurrent": RecurrentNotification, "refund": RefundNotification
}


class AiohttpDispatcher(Router):
    def __init__(self, index: int = None):
        self._web_paths = {}

        super().__init__(index)

    async def process_request(self, request: web.Request) -> web.Response:
        name = self._web_paths[request.url.name]
        notification_type = NOTIFICATION_TYPES.get(name)
        if notification_type is None:
            logger.error(f"notification type {name} not supported")
            return web.json_response(status=500)
        notification = notification_type(**(await request.json(loads=json.loads)))
        result = await self.process_notification(notification)
        if result == Result.INTERNAL_ERROR:
            return web.json_response(status=500)
        if result:
            return web.json_response({"result": result.value})

    def register_app(
            self,
            app: Application,
            path: str,
            pay_path: str = None,
            cancel_path: str = None,
            check_path: str = None,
            confirm_path: str = None,
            fail_path: str = None,
            recurrent_path: str = None,
            refund_path: str = None,
            **kwargs):
        """
        Register route
        All if path doesn't end with "/", sub-paths should start with it and vice-versa
        Only not-null paths are registered :)

        :param app: instance of aiohttp Application
        :param path: route main path
        :param pay_path: sub-path for pay notifications
        :param cancel_path:
        :param check_path:
        :param confirm_path:
        :param fail_path:
        :param recurrent_path:
        :param refund_path:
        :param kwargs:
        """
        paths = {
            "pay": pay_path, "cancel": cancel_path, "check": check_path,
            "confirm": confirm_path, "fail": fail_path,
            "recurrent": recurrent_path, "refund": refund_path
        }
        paths = {k: v for k, v in paths.items() if v is not None}

        for name, path_ in paths.items():
            if path_ is None:
                continue
            self._web_paths[path_.replace("/", "")] = name
            app.router.add_route(
                "POST", path + path_, self.process_request, **kwargs
            )

    def run_app(
            self,
            path: str,
            pay_path: str = None,
            cancel_path: str = None,
            check_path: str = None,
            confirm_path: str = None,
            fail_path: str = None,
            recurrent_path: str = None,
            refund_path: str = None,
            **kwargs
    ):
        """
        Create aiohttp app and run it
        All if path doesn't end with "/", sub-paths should start with it and vice-versa
        Only not-null paths are registered :)

        :param path: route main path
        :param pay_path: sub-path for pay notifications
        :param cancel_path:
        :param check_path:
        :param confirm_path:
        :param fail_path:
        :param recurrent_path:
        :param refund_path:
        :param kwargs:
        """
        app = web.Application()
        self.register_app(
            app, path, pay_path, cancel_path, check_path, confirm_path,
            fail_path, recurrent_path, refund_path, **kwargs
        )
        web.run_app(app)
