#Nothing: None <class 'NoneType'>$
#Cheese: nan <class 'float'>$
#Zero: 0 <class 'int'>$ 
#Empty: <class 'str'>$
#Fake: False <class 'bool'>$
#Type not Found$
#1$
def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
    elif isinstance(object, float):
        print("Cheese: nan", type(object))
    elif isinstance(object, int) and (isinstance(object, bool) == 0):
        print("Zero: 0", type(object))       
    elif isinstance(object, str) and object == "":
        print("Empty:", type(object))
    elif isinstance(object, bool) and object is False:
        print("Fake: False", type(object))
    else:
        print("Type not found")
    return 1