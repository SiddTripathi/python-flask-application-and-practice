#Another use case is that if decorator itself has parameter
#for example if we can have different passwords returning functions for different kind of users
#and we can pass that information in decorator

import functools
from typing import Any, Callable, Dict

#decorator
def make_secure(access_level: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def secure_func(user: dict, *args: Any, **kwargs: Any):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"The user {user['username']} does not have {access_level} permissions"
        return secure_func
    return decorator

#now for our password returning functions, we pass acess level info at method definition level

@make_secure("admin")
def get_admin_password()->str:
    return "admin_passwrd" 

@make_secure("user")
def get_dashboard_password() ->str:
    return "dashboard_password"       


user1  ={"username":"Dom","access_level":"user"}
user2  ={"username":"Jose","access_level":"guest"}
user3  ={"username":"Sidd","access_level":"admin"}

print(get_admin_password(user1))
print(get_dashboard_password(user1))
print(get_admin_password(user2))
print(get_dashboard_password(user2))
print(get_admin_password(user3))
print(get_dashboard_password(user3))