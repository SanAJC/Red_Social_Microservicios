import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

API_ENDPOINTS = {
    'profile': 'http://profile-service:8000/profile/user',
    'feed': 'http://feed-service:8000/feed/',
    'follow': 'http://follow-service:8000/user/followed',
    'notification': 'http://notification-service:8000/user/notifications/',
}

@api_view(['GET'])
def get_profile(request):
    try:
        response = requests.get(f"{API_ENDPOINTS['profile']}")
        response.raise_for_status()  
        data = response.json()
    except requests.RequestException as e:
        data = {'error': str(e)}
    return Response(data)

@api_view(['GET'])
def get_feed(request):
    try:
        response = requests.get(f"{API_ENDPOINTS['feed']}")
        response.raise_for_status() 
        data = response.json()
    except requests.RequestException as e:
        data = {'error': str(e)}
    return Response(data)

@api_view(['GET'])
def get_follow(request):
    try:
        response = requests.get(f"{API_ENDPOINTS['follow']}")
        response.raise_for_status() 
        data = response.json()
    except requests.RequestException as e:
        data = {'error': str(e)}
    return Response(data)
    
@api_view(['GET'])
def get_notification(request):
    try:
        response = requests.get(f"{API_ENDPOINTS['notification']}")
        response.raise_for_status() 
        data = response.json()
    except requests.RequestException as e:
        data = {'error': str(e)}
    return Response(data)


