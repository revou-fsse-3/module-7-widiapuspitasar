from flask_login import current_user
from functools import wraps

def role_required(role_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated and current_user.role == role_name:
                return func(*args, **kwargs)
            else:
                return { "message": "You are not allowed to doing this action to the product because you are not an admin" }
        return wrapper
    return decorator