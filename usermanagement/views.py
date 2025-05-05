from django.shortcuts import render
from django.http import JsonResponse
from usermanagementservice.models import User
from rest_framework.decorators import api_view
import json

@api_view(['PUT'])
def add_user(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")

        if username is None or email is None:
            return JsonResponse({"error": "Missing username or email"}, status=400)
        
        User.objects.create(username=username, email=email)
        return JsonResponse({"error": ""}, status=200)
    except:
        return JsonResponse({"error":"Server error"}, status=500)
