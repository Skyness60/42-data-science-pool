def NULL_not_found(object: any) -> int:
    type_map = {
        type(None): "Nothing : None",
        float: "Cheese: nan",
        bool: "Fake: False",
        int: "Zero: 0",
        str: "Empty: ",
    }
    for t, name in type_map.items():
        if not object or t is float and str(object) == "nan":
            if isinstance(object, t):
                print(name, type(object))
                break
    else:
        print("Type not found")

    return 1
