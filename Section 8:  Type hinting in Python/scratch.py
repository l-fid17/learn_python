from typing import List, Dict, Union

def my_function() -> None: # -> None *type hint*
    pass

# uncomment below and
# hover_over_me = my_function()

def another_func() -> List[Dict(str, Union(str, int))]: # List of Dict(s) each of which has KEYS of type 'str' and values of type "str" and/or "int"
    return [{"a": "a", "b": "b", "c": 0}, {"a": "a", "b": "b", "c": 0}]


data = another_func()
print(data)


"""
Our own Types
"""
Book = Dict(str, Union(str, int))
def again_a_fn(a: str, b: str) -> List[Book]: # type hint for parameters
    return [{"a": a, "b": b, "c": 0}, {"a": "a", "b": "b", "c": 0}]


more_data = again_a_fn("a", "b")
print(more_data)