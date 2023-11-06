

def validate_creds_from_signup_form(UserClass, passes_check_list, username: str, email: str, password: str, confirm_password: str) -> tuple[bool, str]:
    
    check_list = [
        ( "@" in email and len(email.split('@')) == 2, "Email syntax is invalid.", "email" ),
        
        ( not UserClass.objects.filter(username=username).exists(), "Username already exists.", "username" ),
        
        ( len(username) in range(4,13), "Username must be within 4 to 12 characters.", "username" ),
        
        ( not UserClass.objects.filter(email=email).exists(), "Email already exists.", "email" ),
        
        ( len(password) >= 8, "Password must have at least 8 characters." ),
        
        ( password == confirm_password, "Passwords did not match." )
    ]  

    return passes_check_list(check_list)
    


