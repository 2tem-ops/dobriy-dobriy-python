def merge_dicts(*dict1, ignored_keys=None):
    res = {}

    for d in dict1:
        for k, v in d.items():
            if (ignored_keys and k not in ignored_keys) or (ignored_keys is None):
                res[k] = v

    return res