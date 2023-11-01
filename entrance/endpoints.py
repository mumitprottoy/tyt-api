from django.http import HttpResponse
from tools.global_decorators import private
import json

@private
def create_user(request, *args, **kwargs):
    body_unicode = request.body
        