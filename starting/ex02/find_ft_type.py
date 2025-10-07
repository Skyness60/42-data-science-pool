def all_thing_is_obj(obj: any) -> int:
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    for t, name in type_map.items():
        if isinstance(obj, t):
            if t is str:
                print(f"{obj} is in the kitchen : {t}")
            else:
                print(f"{name} : {t}")
            break
    else:
        print("Type not found")

    return 42
