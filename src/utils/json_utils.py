def _keys_s1_in_s2(s1: dict, s2: dict) -> bool:
    for key, value in s1.items():
        if type(value) is not dict:
            if key not in s2.keys():
                return False
        else:
            if type(s2[key]) is not dict:
                return False
            if not _keys_s1_in_s2(value, s2[key]):
                return False
    return True

def same_keys(s1: dict, s2: dict) -> bool:
    return _keys_s1_in_s2(s1, s2) and _keys_s1_in_s2(s2, s1)

