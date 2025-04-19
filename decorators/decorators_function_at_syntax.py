# Decorator functions in Python are used to modify or extend the behavior of functions or methods.
# They are applied using the "@" syntax and are often used for logging, access control, or memoization.

import functools

user  ={"username":"Sidd","access_level":"guest"}




#decorator
def make_secure(func):
    @functools.wraps(func)
    def secure_func():
        if user["access_level"] == "admin":
            return func()
        else:
            return(f"The user {user['username']} does not have admin permissions")
    return secure_func

@make_secure                       #using @ here to tell that get_admin_password cannot be created as is but will be passed to function make_secure
def get_admin_password():
    return "1234"
        

print(get_admin_password())                            #if we call get_admin_password before line 22 then still secure function is bypassed
#get_admin_password = make_secure(get_admin_password)   #Thats where we use a @syntax to ensure that get_admin_password is secured

print(get_admin_password.__name__)       #this line tells that the get_admin_password function is acutally replaced by secure_func and is no longer 
                                         #registered as function internally. Some of the libraries which use that information will now refer to secure
                                         #func() such as __name__. To fix this we use functool wrapper which tells that secure_func is not replacement but wrapper
