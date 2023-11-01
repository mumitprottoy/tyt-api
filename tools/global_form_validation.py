
def form_fields_are_valid(inputs: list, fields: list, csrf=True) -> tuple[bool, list]:
    
    error_msg = 'The form is corrupted. Probably through inspection tools.'
    
    if csrf: fields = ['csrfmiddlewaretoken']+fields
    
    if len(fields)!=len(inputs): 
        return False, [error_msg]
    
    for i in range(len(fields)):  
        if fields[i]!=inputs[i]: 
            return False, [error_msg]
    
    return True, None



# sets the first element of the list type value to each respective key 
def get_rid_of_list_type_values(form_data: dict) -> dict:
    
    for key in form_data.keys():
        if type(form_data[key]) is list:
            form_data[key] = form_data[key][0]
    
    return form_data  
 