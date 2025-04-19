#what if the function which uses decorator has argument to pass

import functools

user  ={"username":"Sidd","access_level":"admin"}




#decorator
def make_secure(func):
    @functools.wraps(func)
    def secure_func(*args,**kwargs):
        if user["access_level"] == "admin":
            return func(*args,**kwargs)
        else:
            return(f"The user {user['username']} does not have admin permissions")
    return secure_func

@make_secure                     
def get_admin_password(panel):
    if panel == "admin":
      return "1234"
    elif panel == "billing":
        return "Super_secure_password"

print(get_admin_password("billing")) #this will give argument error even though we have changed get_admin_password function. Thats because its
                                     #decorator does not take argument. So in order to make decorator a common template we change it to have *args, **kwargs
        

