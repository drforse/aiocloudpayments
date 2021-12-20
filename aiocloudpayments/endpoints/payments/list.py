from typing import List
from datetime import date

from ..base import CpEndpoint, Request
from ...types.transaction_in_list import TransactionInList


class CpPaymentsListEndpoint(CpEndpoint):
    __returning__ = List[TransactionInList]

    date: date
    time_zone: str

    def build_request(self) -> Request:
        return Request(
            endpoint="payments/list",
            x_request_id=self.x_request_id,
            json_str=self.json(exclude={"x_request_id", "x_signature"}, by_alias=True)
        )
