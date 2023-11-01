def passes_check_list(check_list: tuple[bool, str]) -> tuple[bool, str]:
    issues = list()
    for check in check_list:
        if not check[0]: issues.append(check)
    

    return (True, None) if not issues else (False, issues)