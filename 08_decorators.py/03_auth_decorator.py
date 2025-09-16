from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role == "admin":
            return func(user_role)
        return "Access denied"
    return wrapper

@require_admin
def delete_user(user_role):
    return f"User deleted: {user_role}"

print(delete_user("admin"))
print(delete_user("user"))
