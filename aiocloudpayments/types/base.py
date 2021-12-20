import datetime

from pydantic import BaseModel
from pydantic.utils import to_camel


class CpObject(BaseModel):
    class Config:
        # use_enum_values = True
        # orm_mode = True
        # extra = Extra.allow
        # validate_assignment = True
        # allow_mutation = False
        json_encoders = {datetime.datetime: lambda dt: int(dt.timestamp())}
        alias_generator = to_camel
        allow_population_by_field_name = True
