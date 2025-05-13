from helpers.agora_tools.ChatTokenBuilder2 import *
from django.conf import settings
import requests

def generate_user_token(user_id):
    app_id = settings.AGORA["APP_ID"]
    app_certificate = settings.AGORA["APP_CERT"]
    token = ChatTokenBuilder.build_user_token(app_id, app_certificate, user_id, int(time.time()) + 3600)
    return token

def generate_app_token():
    app_id = settings.AGORA["APP_ID"]
    app_certificate = settings.AGORA["APP_CERT"]
    token = ChatTokenBuilder.build_app_token(app_id, app_certificate, int(time.time()) + 3600)
    return token

def add_chat_user(user_id):
    try:
        url = f"{settings.AGORA["CHAT_API"]}/{settings.AGORA["ORG_NAME"]}/{settings.AGORA["APP_NAME"]}/users"
        body = {
            'username': user_id
        }
        app_token = generate_app_token()
        headers = {"Authorization": f"Bearer {app_token}"}

        resp = requests.post(url, json=body, headers=headers)
        return resp.status_code
    except:
        return 500

