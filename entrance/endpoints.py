import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tools.global_decorators import private
from .program_interface import create_user, authenticate_user



@csrf_exempt
@private
def user_creation(request, *args, **kwargs):
    body = kwargs['body']
    response = create_user(body['data'], csrf=body['csrf'])
    return JsonResponse(response) 
    


@csrf_exempt
@private
def user_authentication(request, *args, **kwargs):
    body = kwargs['body']
    response = authenticate_user(body['data'], csrf=body['csrf'])
    return JsonResponse(response) 
        