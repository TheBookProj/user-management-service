from django.shortcuts import render
from django.http import JsonResponse
from usermanagementservice.models import User
from rest_framework.decorators import api_view
from helpers import agora
import json

@api_view(['PUT'])
def add(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")

        if username is None or email is None:
            return JsonResponse({"error": "Missing username or email."}, status=400)
        
        new_user = User.objects.create(username=username, email=email)
        user_id = str(new_user.id)
        status = agora.add_chat_user(user_id)
        if status == 200:
            return JsonResponse({"error": ""}, status=200)
        return JsonResponse({"error": "There was an issue in adding chat user."}, status=status)
    except:
        return JsonResponse({"error":"Server error"}, status=500)

@api_view(['GET'])
def login(request):
    try:
        email = request.GET.get("email", "")

        if email is None:
            return JsonResponse({"error": "Missing email."}, status=400)

        user = User.objects.filter(email=email).first()

        if user is None:
            return JsonResponse({"error": "User not found."}, status=404)

        user_id = str(user.id)
        rtm_token = agora.generate_user_token(user_id)

        return JsonResponse({"error": "", "token": rtm_token, "id": user_id}, status=200)
    except:
        return JsonResponse({"error":"Server error."}, status=500)
