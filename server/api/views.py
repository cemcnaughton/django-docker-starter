# from django.shortcuts import render
# from django.shortcuts import render
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from django.contrib.auth import authenticate,login,logout
# from example_apiproject.serializers import UserSerializer
# from django.db.models import Count
# import sys
# from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes


# @csrf_exempt
# def login_ajax(request):
# 	response = JsonResponse({"error": "Wrong credentials"},status=406)
	
	
# 	body_unicode = request.body.decode('utf-8')
# 	body = json.loads(body_unicode)

# 	username = body['username']
# 	password = body['password']
# 	user = authenticate(username=username, password=password)
# 	if user is not None:
# 		if user.is_active:
# 			login(request, user)
			
# 			user_s = UserSerializer(instance=user)
# 			response = JsonResponse(user_s.data)
# 			# Redirect to a success page.

# 	return response

# def logout_ajax(request):
	
# 	logout(request)
# 	response = JsonResponse({"message":"OK"})
	
# 	return response