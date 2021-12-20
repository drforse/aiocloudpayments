# aiocloudpayments
Python Async [CloudPayments](https://developers.cloudpayments.ru/#api) Library
# Basic Usage Example
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

architecture inspired by [aiogram](https://github.com/aiogram/aiogram)