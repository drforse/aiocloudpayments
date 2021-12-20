import datetime

from pydantic import BaseModel
from pydantic.utils import to_camel

from ..utils import json


class CpObject(BaseModel):
    class Config:
        json_loads = json.loads
        json_dumps = json.dumps
        json_encoders = {datetime.datetime: lambda dt: int(dt.timestamp())}
        alias_generator = to_camel
        allow_population_by_field_name = True
