from django.http import HttpResponse
import json


def private(endpoint):
    def check(request, *args, **kwargs):
        if not request.body:
            return HttpResponse("This is a private API endpoint.")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
    return check            