def int_version(x):
    return x + 10
def str_version(x):
    return x.upper()

dispatch = {
    int: int_version,
    str: str_version
}
def show(x):
    return dispatch[type(x)](x)
print(show(5))        
print(show("amit"))   
