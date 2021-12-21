# aiocloudpayments
Python Async [CloudPayments](https://developers.cloudpayments.ru/#api) Library
# Client Basic Usage Example
```
from datetime import date

from aiocloudpayments import AioCpClient


async def main():
    client = AioCpClient(PUBLIC_ID, API_SECRET)

    await client.test()

    await client.charge_card(
        amount=10,
        currency="RUB",
        invoice_id="1234567",
        ip_address="123.123.123.123",
        description="Payment for goods in example.com",
        account_id="user_x",
        name="CARDHOLDER NAME",
        card_cryptogram_packet="01492500008719030128SMfLeYdKp5dSQVIiO5l6ZCJiPdel4uDjdFTTz1UnXY+3QaZcNOW8lmXg0H670MclS4lI+qLkujKF4pR5Ri+T/E04Ufq3t5ntMUVLuZ998DLm+OVHV7FxIGR7snckpg47A73v7/y88Q5dxxvVZtDVi0qCcJAiZrgKLyLCqypnMfhjsgCEPF6d4OMzkgNQiynZvKysI2q+xc9cL0+CMmQTUPytnxX52k9qLNZ55cnE8kuLvqSK+TOG7Fz03moGcVvbb9XTg1oTDL4pl9rgkG3XvvTJOwol3JDxL1i6x+VpaRxpLJg0Zd9/9xRJOBMGmwAxo8/xyvGuAj85sxLJL6fA==",
        payer=Person(
            first_name="Test",
            last_name="Test",
            middle_name="Test",
            birth=date(1998, 1, 16),
            address="12A, 123",
            street="Test Avenue",
            city="LosTestels, City of Test Angels",
            country="Testland",
            phone="+1 111 11 11",
            post_code="101011010"
        )
    )

    await client.disconnect()
```
# AiohttpDispatcher Basic Usage Example
```
from aiocloudpayments import AiohttpDispatcher, Result
from aiocloudpayments.types import PayNotification, CancelNotification


CERT_FILE = "cert.pem"
CERT_FILE = "pkey.pem"


def main():
    dp = AiohttpDispatcher()

    # router is not needed here, but I am just showing the logic
    router = Router()

    # register with router
    @router.cancel(lambda n: 5 > n.amount > 1)
    async def foo(notification: CancelNotification):
        print(f"{notification=}")
        # return {"result": 0}
        return Result.OK

    # register with router
    @router.pay(lambda n: n.amount <= 1)
    async def foo(notification: PayNotification):
        print(f"{notification.amount=}")
        # return {"result": 12}
        return Result.WRONG_AMOUNT

    # register with dp
    @dp.cancel(lambda n: n.amount > 5)
    async def foo(notification: CancelNotification):
        print(f"{notification.amount=}, > 5")
        # if you don't return anything, Result.OK is assumed

    dp.include_router(router)

    ssl_context = SSLContext()
    ssl_context.load_cert_chain(CERT_FILE, KEY_FILE)

    dp.run_app(
        AioCpClient(PUBLIC_ID, API_SECRET),
        "/test",
        pay_path="/pay",
        cancel_path="/cancel",
        ssl_context=ssl_context,
        check_hmac=False  # disable hmac check, only use in development environments
    )
```

architecture inspired by [aiogram](https://github.com/aiogram/aiogram)