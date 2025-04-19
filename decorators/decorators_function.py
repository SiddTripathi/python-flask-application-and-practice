# Decorator functions in Python are used to modify or extend the behavior of functions or methods.
# They are applied using the "@" syntax and are often used for logging, access control, or memoization.


user  ={"username":"Sidd","access_level":"guest"}

def get_admin_password():
    return "1234"


#decorator
def make_secure(func):
    def secure_func():
        if user["access_level"] == "admin":
            return func()
        else:
            return(f"The user {user['username']} does not have admin permissions")
    return secure_func()
        


get_admin_password = make_secure(get_admin_password)

print(get_admin_password)