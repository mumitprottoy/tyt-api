
# sets the first element of the list type value to each respective key 
def get_rid_of_list_type_values(form_data: dict) -> dict:
    
    for key in form_data.keys():
        if type(form_data[key]) is list:
            form_data[key] = form_data[key][0]
    
    return form_data 