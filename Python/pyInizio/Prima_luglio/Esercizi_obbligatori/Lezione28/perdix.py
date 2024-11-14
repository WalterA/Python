def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] *= value
        else:
            merged_dict[key] = value 
    return merged_dict
