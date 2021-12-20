import logging
from datetime import datetime, date

from pydantic.datetime_parse import parse_date

logger = logging.getLogger(__name__)


class CpUnixDate(date):
    @classmethod
    def __get_validators__(cls):
        def validate(value):
            try:
                return datetime.fromtimestamp(int(value.split("/Date(")[1].split(")/")[0])/1000).date()
            except (IndexError, ValueError):
                logger.warning(f"{cls.__name__} couldn't parse {value}, using pydantic's parse_date")
                return parse_date(value)
        yield validate
