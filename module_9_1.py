def apply_all_func(int_list: list, *functions):
    res_dict: dict = {}
    for func in functions:
        res = func(int_list)
        res_dict[func.__name__] = res
    return res_dict
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))