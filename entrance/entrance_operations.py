
def filter_names(names: list) -> list:
    
    for i in range(len(names)):
        names[i] = names[i].replace('.', '')
        parts = names[i].split()
        
        for j in range(len(parts)): 
            parts[j] = parts[j].lower().capitalize() 
    
        names[i] = ' '.join(parts)
    
    print("filter names", names) 
    return names



def identify_user_or_email(cred:str, UserClass):
    username, email = {"username": cred}, {"email": cred}
    
    if UserClass.objects.filter(**username).exists():
        return True, username
    
    if UserClass.objects.filter(**email).exists():
        return True, email
    
    return False, None
       