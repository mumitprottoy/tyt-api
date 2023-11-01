from tools.global_form_validation import (
    get_rid_of_list_type_values,
    form_fields_are_valid
)
from .entrance_form_validation import validate_creds_from_signup_form
from tools.variables import FORM_FIELDS as ff
from tools.global_operations import passes_check_list
from django.contrib.auth.models import User





# user creation
def get_prefill_context(form_data:dict, fields: list):
    context = form_data.copy()
    for f in fields: context[f] = ""
    context['password'], context['confirm_password'] = ("", "")
    print(context)
    
    return context



def extract_fields(status: tuple):
    return [issues[2] for issues in status[1] if len(issues)>2 and not issues[0]]

def extract_errors(status: tuple):
    return [issues[1] for issues in status[1]]
    



def create_user(form_data: dict, csrf=True) -> tuple[bool, str]:
    form_data = get_rid_of_list_type_values(form_data)
    status = form_fields_are_valid(inputs=list(form_data.keys()), fields=ff['signup'], csrf=csrf)
    
    if status[0]:
        
        from .entrance_operations import filter_names
        form_data['first_name'], form_data['last_name'] = filter_names(
            [
                form_data['first_name'], 
                form_data['last_name']
             ]
        )
        
        status = validate_creds_from_signup_form(
            UserClass = User, 
            passes_check_list = passes_check_list,
            username = form_data['username'],
            email = form_data['email'],
            password = form_data['password'],
            confirm_password = form_data['confirm_password'],
        )

        if status[0]:
            form_data.pop('confirm_password')
            
            if csrf: form_data.pop('csrfmiddlewaretoken')
            pwd = form_data['password']
            new_user = User(**form_data)
            new_user.set_password(pwd)
            new_user.save()
            
            return {
                "created": True,
            }
        
        else: 
            return {
                "created": False,
                "errors": extract_errors(status),
                "prefill": get_prefill_context(form_data, extract_fields(status))
            }
            
    
    return {
        "created": False,
        "errors": status[1]
    }

 
 
 # login
 
def authenticate_user(request, form_data: dict) -> tuple[bool, str]:
    form_data = get_rid_of_list_type_values(form_data)
    status = form_fields_are_valid(inputs=list(form_data.keys()), fields=ff['signin'])
    
    if status[0]:
        from .entrance_operations import identify_user_or_email
        
        identified = identify_user_or_email(form_data['username_or_email'], User)
        
        if identified[0]:
            user = User.objects.get(**identified[1])
            creds = {'username': user.username, 'password': form_data['password']}
        else: return False, ["invalid username or email."]
        
        
        from django.contrib.auth import authenticate, login
        if authenticate(**creds):
            login(request, user)
            
            return True, None
        
        else: return False, ['Wrong password.'], {'username': user.username}
    
    return status
            