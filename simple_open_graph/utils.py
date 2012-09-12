def string_to_dict(string):
    kwargs = {}
    if string:
        string = str(string)
        for arg in string.split(','):
            arg = arg.strip()
            key, value = arg.split('=', 1)
            kwargs[key] = value
    return kwargs
