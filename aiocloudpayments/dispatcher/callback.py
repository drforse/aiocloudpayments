import enum


class Result(enum.Enum):
    """
    if callback doesn't return anything -> Result.OK is assumed

    Result.INTERNAL_ERROR: tell dispatcher to return status 500
    Result.SKIP: tell routers to skip this handler
    """
    OK = 0
    WRONG_ORDER_NUMBER = 10
    WRONG_ACCOUNT_ID = 11
    WRONG_AMOUNT = 12
    PAYMENT_CANT_BE_TAKEN = 13
    PAYMENT_EXPIRED = 20

    INTERNAL_ERROR = 500
    SKIP = 501
