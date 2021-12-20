from typing import Any

from .base import CpObject


class Secure3D(CpObject):
    transaction_id: int
    pa_req: str
    acs_url: str
    go_req: Any = None
    three_ds_session_data: Any = None
    iframe_is_allowed: bool = None
    frame_width: Any = None
    frame_height: Any = None
    three_ds_callback_id: str = None
    escrow_accumulation_id: Any = None
