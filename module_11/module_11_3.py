def get_introspection_info(obj):
    info_dict = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [met for met in dir(obj) if callable(getattr(obj, met))],
        'module': get_introspection_info.__module__
    }
    return info_dict

number_info = get_introspection_info(42)
print(number_info)