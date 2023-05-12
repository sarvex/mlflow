def strip_prefix(original, prefix):
    return original[len(prefix) :] if original.startswith(prefix) else original


def strip_suffix(original, suffix):
    if original.endswith(suffix) and suffix != "":
        return original[: -len(suffix)]
    return original


def is_string_type(item):
    return isinstance(item, str)
