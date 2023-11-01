import os
import json
from django.http import HttpResponse, JsonResponse
from .variables import (
    HTTP_RESPS,
    JSON_MSG
)


# Enpoints wrapped with this decorator can only be accessed with a private token
def private(endpoint):
    
    def check(request, *args, **kwargs):
        
        if not request.body:
            return HttpResponse(HTTP_RESPS['private'])
        
        # decode and convert into dict
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        
        if body['token'] == os.environ['TYT_API_TOKEN']: 
            return endpoint(request, body=body)
        
        return JsonResponse({"message": JSON_MSG[401]}, status=401)
           
    return check            