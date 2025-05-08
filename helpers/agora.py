from agora_token_builder import RtmTokenBuilder
from django.conf import settings

def generate_rtm_token(user_id):
    app_id = settings.AGORA["APP_ID"]
    app_certificate = settings.AGORA["APP_CERT"]
    token = RtmTokenBuilder.buildToken(app_id, app_certificate, user_id, 1, int(time.time()) + 3600)
    return token