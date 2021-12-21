import hashlib
import hmac
import base64


def hmac_check(message: bytes, api_secret: str, content_hmac: str) -> bool:
    subscription_secret = bytes(api_secret, 'utf-8')

    subscription_signature = base64.b64encode(
        hmac.new(subscription_secret, message, digestmod=hashlib.sha256).digest()
    ).decode('utf-8')

    content_hmac = content_hmac

    return subscription_signature == content_hmac
