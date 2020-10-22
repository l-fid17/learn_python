# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}

# delete_database() function
def delete_database():
    # perform deletion
    print('Database deleted!')


# Define a check_permission() decorator:
def check_permission(func):
    def secure_func():
        if user.get('role') == "admin":
            return func()
        else:
            raise PermissionError("You are not an admin")
    return secure_func

# Use the check_permission() decorator and delete_database() function to create a secure_delete_database() function:
secure_delete_database = check_permission(delete_database)
secure_delete_database()

"""
so the above is the same as below
"""
@check_permission
def delete_database():
    # perform deletion
    print('Database deleted!')

# and we can call the function directly
delete_database()

# however this expose some problems like:
print(delete_database.__name__) # would return `secure_func`
print(delete_database.__doc__) # would return secure_func's doc instead

"""
SOLUTION
functools wraps
"""

import functools

def check_permission(func):
    @functools.wraps(func)      # this tells python we are wrapping our function with secure_func, "extending it's functionality"
    def secure_func():
        if user.get('role') == "admin":
            return func()
        else:
            raise PermissionError("You are not an admin")
    return secure_func

# so now
print(delete_database.__name__) # would return `delete_database`
print(delete_database.__doc__) # would return delete_database's doc instead


"""
decorated funcs with parameters
"""
@check_permission
def delete_with_params(panel):
    return f"Password for {panel} is 1234."

# to achieve the above the decorator should look like this

def check_permission(func):
    @functools.wraps(func)      # this tells python we are wrapping our function with secure_func, "extending it's functionality"
    def secure_func(panel):
        if user.get('role') == "admin":
            return func(panel)
        else:
            raise PermissionError("You are not an admin")
    return secure_func

# problem is that we can then only use the decorator for delete_with_params function

@user_has_permission
def another():
    return "Hello"

another() # calling this function would return an error as the secure_func decorator is missing a parameter
# ... more on it later down below ...

"""
decorators with parameters
"""
# we want to do this
@check_permission("admin") # instead of hardcoding it in the check_permission func
def my_function():
    pass

# so the decorator should look like this
def yet_another_decorator(access_level)
    def check_permission(func):
        @functools.wraps(func)      # this tells python we are wrapping our function with secure_func, "extending it's functionality"
        def secure_func(panel):
            if user.get('role') == access_level:
                return func(panel)
            else:
                raise PermissionError("You are not an admin")
        return secure_func
    return check_permission

# and when we want to decorate our function we end up with
@yet_another_decorator("admin")
def my_function(panel):
    pass

"""
generic decorators
"""
def yet_another_decorator(access_level)
    def check_permission(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):   # this way we tell python we it could receive optional arguments, either tuples or dictionaries to be unpacked
            if user.get('role') == access_level:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You are not an admin")
        return secure_func
    return check_permission

# and now we can use the decorator with any function